#!/usr/bin/env python3
"""
Simple server to serve the enhanced UI with sidebar
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = '/examples/ui.html'
        return super().do_GET()

def start_ui_server(port=8080):
    """Start the UI server"""
    try:
        # Change to the project root directory
        os.chdir(Path(__file__).parent)
        
        # Create server
        with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
            print("🎮 AI for Engineers - Enhanced UI Server")
            print("=" * 50)
            print(f"🌐 UI Server: http://localhost:{port}")
            print(f"📱 Network: http://0.0.0.0:{port}")
            print("=" * 50)
            print("✨ New Features:")
            print("  • ChatGPT-like sidebar with chat history")
            print("  • Interactive learning games")
            print("  • User settings panel")
            print("  • Larger mathematical background patterns")
            print("=" * 50)
            print("💡 Make sure API server is running on port 5001:")
            print("   python3 api/demo_math_api.py")
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
        print("\n\n🛑 UI Server stopped by user")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use!")
            print(f"💡 Trying port {port + 1}...")
            start_ui_server(port + 1)
        else:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    start_ui_server()