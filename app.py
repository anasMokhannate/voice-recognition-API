from flask import Flask
from app.routes.voice_agents import voice_bp, select_language, select_operation, select_operation_type

app = Flask(__name__)
app.register_blueprint(voice_bp, url_prefix="/api/v1/voice")
app.register_blueprint(select_operation_type, url_prefix="/api/v1/voice")
app.register_blueprint(select_operation, url_prefix="/api/v1/voice")
app.register_blueprint(select_language, url_prefix="/api/v1/voice")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)