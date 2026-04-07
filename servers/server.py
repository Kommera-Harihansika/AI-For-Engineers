#!/usr/bin/env python3
"""
Simple HTTP server for AI for Engineers application
Serves the single-page application on localhost
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = '/app.html'
        return super().do_GET()

def start_server(port=8000):
    """Start the local server"""
    try:
        # Change to the directory containing app.html
        os.chdir(Path(__file__).parent)
        
        # Create server
        with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
            print("🚀 AI for Engineers - Local Server Starting...")
            print("=" * 50)
            print(f"🌐 Server running at: http://localhost:{port}")
            print(f"📱 Network access: http://0.0.0.0:{port}")
            print("=" * 50)
            print("✨ Features available:")
            print("  • Enhanced Mathematical AI")
            print("  • Step-by-step solutions")
            print("  • Interactive learning games")
            print("  • M1-M4 Engineering Mathematics")
            print("=" * 50)
            print("💡 Open your browser and go to:")
            print(f"   http://localhost:{port}")
            print("\n🛑 Press Ctrl+C to stop the server")
            print("=" * 50)
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{port}')
                print("🌐 Opening browser automatically...")
            except:
                print("⚠️  Could not open browser automatically")
                print(f"   Please manually open: http://localhost:{port}")
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use!")
            print(f"💡 Trying port {port + 1}...")
            start_server(port + 1)
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)

if __name__ == "__main__":
    start_server()