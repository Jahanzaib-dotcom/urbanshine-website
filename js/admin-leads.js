/**
 * Urban Shine Perth - Central Leads Management Engine
 * Handles saving, reading, updating, and exporting customer enquiries.
 */

(function () {
  'use strict';

  const STORAGE_KEY = 'urbanshine_leads';
  const SETTINGS_KEY = 'urbanshine_admin_settings';

  const DEFAULT_SETTINGS = {
    whatsappNumber: '+61432979551',
    businessName: 'Urban Shine Perth',
    emailNotifications: true,
    soundAlerts: true
  };

  // Seed sample leads matching Perth service scope
  const SEED_LEADS = [
    {
      id: 'US-2026-101',
      name: 'Sarah Connor',
      company: 'Skynet Perth Facility',
      phone: '0432 979 551',
      email: 's.connor@skynet.com.au',
      suburb: 'Perth CBD (6000)',
      service: 'Carpet Steam Cleaning',
      scope: 'Commercial (3 Floors)',
      date: '2026-09-18',
      time: '14:00',
      status: 'New',
      notes: 'High-traffic lobby and boardroom carpet deep steam extraction.',
      source: 'Homepage Booking Modal',
      createdAt: new Date(Date.now() - 3600000).toISOString()
    },
    {
      id: 'US-2026-102',
      name: 'David Miller',
      company: 'Residential Property',
      phone: '0412 884 921',
      email: 'david.miller@westnet.com.au',
      suburb: 'Cottesloe (6011)',
      service: 'Complete Timber Floor Restoration',
      scope: '4 Bedrooms + Living',
      date: '2026-09-19',
      time: '09:30',
      status: 'Pending',
      notes: 'Heritage Jarrah floor sanding, scratch repair, and satin polyurethane seal.',
      source: 'Book Online Page',
      createdAt: new Date(Date.now() - 14400000).toISOString()
    },
    {
      id: 'US-2026-103',
      name: 'Elena Rossi',
      company: 'Rossi Cafe & Bistro',
      phone: '0421 556 709',
      email: 'elena@rossicafe.com.au',
      suburb: 'Scarborough (6019)',
      service: 'Rotary Tile & Grout Deep Cleaning',
      scope: 'Commercial Kitchen & Dining',
      date: '2026-09-20',
      time: '06:00',
      status: 'Confirmed',
      notes: 'Commercial kitchen quarry tile descaling and dining area porcelain grout restoration.',
      source: 'Service Page Quote',
      createdAt: new Date(Date.now() - 86400000).toISOString()
    }
  ];

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
        if (!data) {
          localStorage.setItem(STORAGE_KEY, JSON.stringify(SEED_LEADS));
          return [...SEED_LEADS];
        }
        return JSON.parse(data);
      } catch (e) {
        console.error('Failed to read leads:', e);
        return [...SEED_LEADS];
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
      const nextNum = leads.length > 0 
        ? Math.max(...leads.map(l => parseInt((l.id || '').replace(/\D/g, '') || '0'))) + 1 
        : 101;
      
      const newLead = {
        id: `US-2026-${nextNum}`,
        name: leadData.name || 'Anonymous Client',
        company: leadData.company || leadData.suburb || 'Residential Customer',
        phone: leadData.phone || '',
        email: leadData.email || '',
        suburb: leadData.suburb || 'Perth Metro',
        service: leadData.service || 'General Cleaning Enquiry',
        scope: leadData.scope || 'Standard Inspection',
        date: leadData.date || new Date().toISOString().split('T')[0],
        time: leadData.time || '10:00',
        status: 'New',
        notes: leadData.notes || '',
        source: leadData.source || 'Website Form',
        urgency: leadData.urgency || 'Standard',
        createdAt: new Date().toISOString()
      };

      leads.unshift(newLead);
      this.saveLeads(leads);

      // Play subtle chime if audio is supported and enabled
      if (this.getSettings().soundAlerts) {
        this.playNotificationSound();
      }

      console.log('Urban Shine Lead Logged:', newLead);
      return newLead;
    },

    updateLead(id, updates) {
      const leads = this.getLeads();
      const index = leads.findIndex(l => l.id === id);
      if (index !== -1) {
        leads[index] = { ...leads[index], ...updates };
        this.saveLeads(leads);
        return leads[index];
      }
      return null;
    },

    deleteLead(id) {
      const leads = this.getLeads().filter(l => l.id !== id);
      this.saveLeads(leads);
      return leads;
    },

    resetToDemo() {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(SEED_LEADS));
      window.dispatchEvent(new CustomEvent('urbanshine_leads_changed', { detail: SEED_LEADS }));
      return [...SEED_LEADS];
    },

    clearAll() {
      localStorage.setItem(STORAGE_KEY, JSON.stringify([]));
      window.dispatchEvent(new CustomEvent('urbanshine_leads_changed', { detail: [] }));
      return [];
    },

    getMetrics() {
      const leads = this.getLeads();
      const total = leads.length;
      const pending = leads.filter(l => l.status === 'New' || l.status === 'Pending').length;
      const active = leads.filter(l => l.status === 'Confirmed' || l.status === 'In Progress').length;
      const won = leads.filter(l => l.status === 'Completed' || l.status === 'Won').length;

      // Group by service
      const byService = {};
      leads.forEach(l => {
        const s = l.service || 'General Service';
        byService[s] = (byService[s] || 0) + 1;
      });

      return { total, pending, active, won, byService };
    },

    exportCSV() {
      const leads = this.getLeads();
      if (!leads.length) {
        alert('No leads available to export.');
        return;
      }

      const headers = ['Lead ID', 'Date Created', 'Customer Name', 'Company/Type', 'Phone', 'Email', 'Suburb', 'Service', 'Scope', 'Preferred Date', 'Status', 'Source', 'Notes'];
      const rows = leads.map(l => [
        `"${l.id || ''}"`,
        `"${l.createdAt || ''}"`,
        `"${(l.name || '').replace(/"/g, '""')}"`,
        `"${(l.company || '').replace(/"/g, '""')}"`,
        `"${l.phone || ''}"`,
        `"${l.email || ''}"`,
        `"${(l.suburb || '').replace(/"/g, '""')}"`,
        `"${(l.service || '').replace(/"/g, '""')}"`,
        `"${(l.scope || '').replace(/"/g, '""')}"`,
        `"${l.date || ''} ${l.time || ''}"`,
        `"${l.status || 'New'}"`,
        `"${(l.source || '').replace(/"/g, '""')}"`,
        `"${(l.notes || '').replace(/"/g, '""')}"`
      ]);

      const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
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
        osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
        osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.15); // A5
        gain.gain.setValueAtTime(0.12, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.3);
      } catch (e) {
        // AudioContext may be blocked before interaction
      }
    }
  };

  window.UrbanShineLeads = UrbanShineLeads;
})();
