from flask import Flask
from app.routes.voice_agents import voice_bp

app = Flask(__name__)
app.register_blueprint(voice_bp, url_prefix="/api/voice")
app.register_blueprint(voice_bp, url_prefix="/api/voice/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)