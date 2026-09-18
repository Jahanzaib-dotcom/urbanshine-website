import http.server
import socketserver
import json
import os

PORT = 8088
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
LEADS_FILE = os.path.join(DIRECTORY, "leads.json")

if not os.path.exists(LEADS_FILE):
    with open(LEADS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)

class LeadHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/leads" or self.path.startswith("/api/leads?"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            try:
                with open(LEADS_FILE, "r", encoding="utf-8") as f:
                    data = f.read()
                self.wfile.write(data.encode("utf-8"))
            except Exception:
                self.wfile.write(b"[]")
            return

        if self.path == "/admin":
            self.path = "/admin.html"

        super().do_GET()

    def do_POST(self):
        if self.path == "/api/leads":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            try:
                payload = json.loads(body)
                leads = []
                if os.path.exists(LEADS_FILE):
                    try:
                        with open(LEADS_FILE, "r", encoding="utf-8") as f:
                            leads = json.load(f)
                    except Exception:
                        leads = []

                if payload.get("action") == "clear":
                    leads = []
                elif payload.get("name") or payload.get("id"):
                    existing_idx = next((i for i, l in enumerate(leads) if l.get("id") == payload.get("id")), -1)
                    if existing_idx != -1:
                        leads[existing_idx] = {**leads[existing_idx], **payload}
                    else:
                        leads.insert(0, payload)

                with open(LEADS_FILE, "w", encoding="utf-8") as f:
                    json.dump(leads, f, indent=2)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "lead": payload, "total": len(leads)}).encode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return

        super().do_GET()

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), LeadHandler) as httpd:
        print(f"Urban Shine server running with API at http://localhost:{PORT}")
        httpd.serve_forever()
