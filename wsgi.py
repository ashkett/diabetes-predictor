from waitress import serve
import app

print("Starting server...")
serve(app.app, host='0.0.0.0', port=8000)