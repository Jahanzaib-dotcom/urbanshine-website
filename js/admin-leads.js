/**
 * Urban Shine Perth - Real-Time Leads Management Engine
 * Captures live customer queries directly from website quote forms.
 * Synchronizes across localStorage and /api/leads backend.
 * Zero hardcoded mock data.
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'urbanshine_leads';
  const SETTINGS_KEY = 'urbanshine_admin_settings';

  const DEFAULT_SETTINGS = {
    whatsappNumber: '+61432979551',
    businessName: 'Urban Shine Perth',
    soundAlerts: true
  };

  const UrbanShineLeads = {
    getSettings() {
      try {
        const saved = localStorage.getItem(SETTINGS_KEY);
        return saved ? { ...DEFAULT_SETTINGS, ...JSON.parse(saved) } : { ...DEFAULT_SETTINGS };
      } catch (e) {
        return { ...DEFAULT_SETTINGS };
      }
    },

    saveSettings(newSettings) {
      try {
        const current = this.getSettings();
        const updated = { ...current, ...newSettings };
        localStorage.setItem(SETTINGS_KEY, JSON.stringify(updated));
        window.dispatchEvent(new CustomEvent('urbanshine_settings_updated', { detail: updated }));
        return updated;
      } catch (e) {
        console.error('Failed to save settings:', e);
      }
    },

    getLeads() {
      try {
        const data = localStorage.getItem(STORAGE_KEY);
        if (!data) return [];
        const leads = JSON.parse(data);
        // Exclude any legacy test records
        const realLeads = leads.filter(l => 
          l && l.name && l.name !== 'Sarah Connor' && l.name !== 'David Miller' && l.name !== 'Elena Rossi'
        );
        if (realLeads.length !== leads.length) {
          localStorage.setItem(STORAGE_KEY, JSON.stringify(realLeads));
        }
        return realLeads;
      } catch (e) {
        console.error('Failed to read leads:', e);
        return [];
      }
    },

    saveLeads(leads) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(leads));
        window.dispatchEvent(new CustomEvent('urbanshine_leads_changed', { detail: leads }));
      } catch (e) {
        console.error('Failed to write leads:', e);
      }
    },

    addLead(leadData) {
      const leads = this.getLeads();
      const timestamp = new Date();
      const nextNum = leads.length + 1;
      const leadId = `US-${timestamp.getFullYear()}-${String(nextNum).padStart(3, '0')}`;

      const newLead = {
        id: leadId,
        name: leadData.name || 'Website Customer',
        company: leadData.company || leadData.suburb || 'Residential Enquiry',
        phone: leadData.phone || '',
        email: leadData.email || '',
        suburb: leadData.suburb || 'Perth Metro',
        service: leadData.service || 'General Enquiry',
        scope: leadData.scope || leadData.urgency || 'Standard Free Assessment',
        date: leadData.date || timestamp.toISOString().split('T')[0],
        time: leadData.time || '',
        status: 'New',
        notes: leadData.notes || '',
        source: leadData.source || 'Website Form Submission',
        urgency: leadData.urgency || 'Standard',
        createdAt: timestamp.toISOString()
      };

      // 1. Immediately store in client localStorage
      leads.unshift(newLead);
      this.saveLeads(leads);

      // 2. Asynchronously sync to backend API (Vercel serverless / server.py)
      try {
        fetch('/api/leads', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newLead)
        }).then(r => r.json()).then(res => {
          console.log('Lead synced to server API:', res);
        }).catch(err => {
          // Local fallback silently maintains state in localStorage
          console.log('API sync notice:', err.message);
        });
      } catch (e) {
        // Ignored
      }

      if (this.getSettings().soundAlerts) {
        this.playNotificationSound();
      }

      console.log('Real Lead Logged to Admin:', newLead);
      return newLead;
    },

    syncWithServer(callback) {
      fetch('/api/leads')
        .then(r => r.json())
        .then(remoteLeads => {
          if (Array.isArray(remoteLeads) && remoteLeads.length > 0) {
            const localLeads = this.getLeads();
            const existingIds = new Set(localLeads.map(l => l.id));
            let added = false;
            remoteLeads.forEach(rLead => {
              if (rLead && rLead.id && !existingIds.has(rLead.id)) {
                localLeads.push(rLead);
                existingIds.add(rLead.id);
                added = true;
              }
            });
            if (added) {
              localLeads.sort((a, b) => new Date(b.createdAt || 0) - new Date(a.createdAt || 0));
              this.saveLeads(localLeads);
            }
          }
          if (callback) callback(this.getLeads());
        })
        .catch(() => {
          if (callback) callback(this.getLeads());
        });
    },

    updateLead(id, updates) {
      const leads = this.getLeads();
      const index = leads.findIndex(l => l.id === id);
      if (index !== -1) {
        leads[index] = { ...leads[index], ...updates };
        this.saveLeads(leads);
        try {
          fetch('/api/leads', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id, ...updates })
          }).catch(() => {});
        } catch (e) {}
        return leads[index];
      }
      return null;
    },

    deleteLead(id) {
      const leads = this.getLeads().filter(l => l.id !== id);
      this.saveLeads(leads);
      return leads;
    },

    clearAll() {
      localStorage.setItem(STORAGE_KEY, JSON.stringify([]));
      try {
        fetch('/api/leads', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ action: 'clear' })
        }).catch(() => {});
      } catch (e) {}
      window.dispatchEvent(new CustomEvent('urbanshine_leads_changed', { detail: [] }));
      return [];
    },

    getMetrics() {
      const leads = this.getLeads();
      const total = leads.length;
      const pending = leads.filter(l => (l.status || 'New') === 'New' || l.status === 'Pending').length;
      const active = leads.filter(l => l.status === 'Confirmed' || l.status === 'In Progress').length;
      const won = leads.filter(l => l.status === 'Completed' || l.status === 'Won').length;

      const byService = {};
      leads.forEach(l => {
        const s = l.service || 'General Cleaning';
        byService[s] = (byService[s] || 0) + 1;
      });

      return { total, pending, active, won, byService };
    },

    exportCSV() {
      const leads = this.getLeads();
      if (!leads.length) {
        alert('No enquiries logged yet. Real submissions from your website forms will appear here.');
        return;
      }

      const headers = ['Lead ID', 'Timestamp', 'Customer Name', 'Location / Suburb', 'Phone', 'Email', 'Service', 'Scope / Urgency', 'Appointment Date', 'Status', 'Source Form', 'Notes'];
      const rows = leads.map(l => [
        `"${l.id || ''}"`,
        `"${l.createdAt || ''}"`,
        `"${(l.name || '').replace(/"/g, '""')}"`,
        `"${(l.suburb || l.company || '').replace(/"/g, '""')}"`,
        `"${l.phone || ''}"`,
        `"${l.email || ''}"`,
        `"${(l.service || '').replace(/"/g, '""')}"`,
        `"${(l.scope || '').replace(/"/g, '""')}"`,
        `"${l.date || ''} ${l.time || ''}"`,
        `"${l.status || 'New'}"`,
        `"${(l.source || '').replace(/"/g, '""')}"`,
        `"${(l.notes || '').replace(/"/g, '""')}"`
      ]);

      const csvContent = 'data:text/csv;charset=utf-8,\uFEFF' + [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement('a');
      link.setAttribute('href', encodedUri);
      link.setAttribute('download', `urbanshine_leads_${new Date().toISOString().split('T')[0]}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    },

    playNotificationSound() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(587.33, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.15);
        gain.gain.setValueAtTime(0.12, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.3);
      } catch (e) {
        // Ignored
      }
    }
  };

  window.UrbanShineLeads = UrbanShineLeads;
})();
