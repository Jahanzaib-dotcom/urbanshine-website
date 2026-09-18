// Vercel Serverless Function: /api/leads
// Stores and returns real-time website leads

let inMemoryLeads = [];

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method === 'POST') {
    try {
      const payload = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
      if (payload) {
        if (payload.action === 'clear') {
          inMemoryLeads = [];
          return res.status(200).json({ success: true, total: 0 });
        }
        if (payload.name || payload.id) {
          const idx = inMemoryLeads.findIndex(l => l.id === payload.id);
          if (idx !== -1) {
            inMemoryLeads[idx] = { ...inMemoryLeads[idx], ...payload };
          } else {
            inMemoryLeads.unshift(payload);
          }
        }
      }
      return res.status(200).json({ success: true, lead: payload, total: inMemoryLeads.length });
    } catch (e) {
      return res.status(400).json({ error: 'Invalid lead payload' });
    }
  }

  if (req.method === 'GET') {
    return res.status(200).json(inMemoryLeads);
  }

  return res.status(405).json({ error: 'Method not allowed' });
}
