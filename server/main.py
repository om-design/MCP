from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define stub tool functions matching your manifest
def analyze_document(document):
    return {"result": f"Stub: analyzed document: {document[:40]}..."}

def detect_bias(content):
    return {"result": f"Stub: bias detected in content: {content[:40]}..."}

def verify_claim(claim):
    return {"result": f"Stub: claim verification for: {claim[:40]}..."}

def evidence_map(claim):
    return {"result": f"Stub: evidence mapped for: {claim[:40]}..."}

def summarize_alternatives(topic):
    return {"result": f"Stub: listed alternatives for: {topic[:40]}..."}

def export_report(report_type):
    return {"result": f"Stub: exported report type: {report_type}"}

def has_needs_status(investigation):
    return {"result": f"Stub: Has/Needs status for: {investigation[:40]}..."}

# HTTP request handler (for Claude/desktop extension to communicate)
class MCPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len)
        data = json.loads(body.decode())
        tool = data.get("tool")
        args = data.get("args", {})

        # Route request to correct stub tool
        if tool == "analyze_document":
            response = analyze_document(args.get("document", ""))
        elif tool == "detect_bias":
            response = detect_bias(args.get("content", ""))
        elif tool == "verify_claim":
            response = verify_claim(args.get("claim", ""))
        elif tool == "evidence_map":
            response = evidence_map(args.get("claim", ""))
        elif tool == "summarize_alternatives":
            response = summarize_alternatives(args.get("topic", ""))
        elif tool == "export_report":
            response = export_report(args.get("report_type", ""))
        elif tool == "has_needs_status":
            response = has_needs_status(args.get("investigation", ""))
        else:
            response = {"error": "Unknown tool"}

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=MCPHandler, port=8080):
    server = server_class(('', port), handler_class)
    print(f'Starting MCP server on port {port}')
    server.serve_forever()

if __name__ == "__main__":
    run()
