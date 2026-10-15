"""
Digital Twin AI — Application Entry Point

Run this file to start the Flask development server or for Vercel deployment.
"""
import os

# Auto-mount Firebase Service Account JSON when running on Vercel
if 'FIREBASE_SERVICE_ACCOUNT_JSON' in os.environ and not os.path.exists('serviceAccountKey.json'):
    with open('/tmp/serviceAccountKey.json', 'w', encoding='utf-8') as f:
        f.write(os.environ['FIREBASE_SERVICE_ACCOUNT_JSON'])
    os.environ['FIREBASE_CREDENTIALS_PATH'] = '/tmp/serviceAccountKey.json'

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=app.config.get('DEBUG', True),
    )
