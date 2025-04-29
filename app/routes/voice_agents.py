from flask import Blueprint, request, jsonify
import whisper  # type: ignore
import requests
import tempfile
import app.utils.prompts.prompts as prompts
import os

voice_bp = Blueprint("voice", __name__)
select_language = Blueprint("select_language", __name__)
select_operation = Blueprint("select_operation", __name__)
select_operation_type = Blueprint("select_operation_type", __name__)


prompt_select_operation = prompts.PROMPT_SELECT_OPERATION
prompt_select_language = prompts.PROMPT_SELECT_LANGUAGE
prompt_select_operation_type = prompts.PROMPT_SELECT_OPERATION_TYPE
prompt_select_operation_confirmation = prompts.PROMPT_SELECT_OPERATION_CONFIRMATION


# Load the Whisper model
model = whisper.load_model("base")

OLLAMA_URL = os.getenv("OLLAMA_URL")  # updated endpoint
OLLAMA_MODEL = "gemma3:1b"

@voice_bp.route("/", methods=["POST"])
def process_voice():
    if "file" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files["file"]

    transcription = transcribe(audio_file)
    if not transcription:
         return jsonify({"error": "Transcription failed"}), 500
    return detect_intention(transcription)


# This function transcribes the audio file using Whisper
def transcribe(audio_file):
    if audio_file is None:
        return jsonify({"error": "No audio file provided"}), 400
    if audio_file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        audio_file.save(tmp.name)
        transcription = model.transcribe(tmp.name)["text"]
    return transcription


# This function sends the transcription to the Ollama model for intention detection
def detect_intention(prompt): 
    input = prompts.MISSION + prompt
    ollama_payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "user",
                "content": input
            }
        ],
        "format": {
            "type": "object",
            "properties": {
                "intent": {
                    "type": "String"
                },
                "amount": {
                    "type": "number"
                }
            },
            "required": [
                "intent",
                "amount"
            ]
        },
        "stream": False,
        "options": {
            "temperature": 0.8,
        },
    }

    try:
        response = requests.post(OLLAMA_URL + "/api/chat", json=ollama_payload)
        print(f"Response : {str(response.text)}")
        response.raise_for_status()
        data = response.json()
        # Extract the actual model response
        model_reply = data.get("message", {}).get("content", "")
    except requests.RequestException as e:
        return jsonify({"error": "Ollama request failed", "details": str(e)}), 500
    except ValueError:
        return jsonify({"error": "Invalid JSON returned from Ollama"}), 500

    return jsonify({
        "transcription": prompt,
        "ollama_response": jsonify(model_reply)
    })
