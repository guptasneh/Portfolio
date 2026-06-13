"""
Flask backend server for portfolio database integration
"""
from flask import Flask, send_from_directory
from flask_cors import CORS
import logging

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



# ═══════════════════════════════════════════════════════════════
# Static Files
# ═══════════════════════════════════════════════════════════════

@app.route('/')
def serve_index():
    """Serve index.html"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files (CSS, JS, images, etc.)"""
    return send_from_directory('.', path)

# ═══════════════════════════════════════════════════════════════
# API Endpoints
# ═══════════════════════════════════════════════════════════════

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Server is running'}), 200



# ═══════════════════════════════════════════════════════════════
# Error Handlers
# ═══════════════════════════════════════════════════════════════

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("🚀 Portfolio Backend Server")
    print("=" * 60)
    print("📡 Server running at: http://localhost:5000")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='localhost', port=5000)
