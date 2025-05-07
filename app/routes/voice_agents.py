from flask import Blueprint, request, jsonify
import app.utils.prompts as prompts
import app.services.ollama_service as ollama_service
from app.services.ollama_service import transcribe
import app.utils.utils as utils


voice_bp = Blueprint("voice", __name__)
select_language = Blueprint("select_language", __name__)
select_operation = Blueprint("select_operation", __name__)
select_operation_type = Blueprint("select_operation_type", __name__)
confirmation = Blueprint("confirmation", __name__)
amount = Blueprint("amount", __name__)


# Load the Whisper model



@select_language.route("/select-language", methods=["POST"])
def select_langauge():

    audio_file = utils.get_file_from_request(request)

    transcription = transcribe(audio_file)
    if not transcription:
         return jsonify({"error": "Transcription failed"}), 500
    return ollama_service.sendLanguageRequest(prompts.prompt_select_language +"\n"+ transcription)



@select_operation.route("/select-operation", methods=["POST"])
def select_operation():

    audio_file = utils.get_file_from_request(request)

    transcription = transcribe(audio_file)
    if not transcription:
         return jsonify({"error": "Transcription failed"}), 500
    return ollama_service.sendOperationRequest(prompts.prompt_select_operation + "\n" + transcription)



@select_operation_type.route("/select-operation-type", methods=["POST"])
def select_operation_type():

    audio_file = utils.get_file_from_request(request)

    transcription = transcribe(audio_file)
    if not transcription:
         return jsonify({"error": "Transcription failed"}), 500
    return ollama_service.sendRequest(prompts.prompt_select_operation_type + "\n" + transcription)


@confirmation.route("/confirmation", methods=["POST"])
def select_operation_type():

    audio_file = utils.get_file_from_request(request)

    transcription = transcribe(audio_file)
    if not transcription:
         return jsonify({"error": "Transcription failed"}), 500
    return ollama_service.sendRequest(prompts.prompt_select_operation_type + "\n" + transcription)


@amount.route("/amount", methods=["POST"])
def provide_amount():

    audio_file = utils.get_file_from_request(request)

    transcription = transcribe(audio_file)
    if not transcription:
         return jsonify({"error": "Transcription failed"}), 500
    return ollama_service.sendRequest(prompts.prompt_select_operation_type + "\n" + transcription)
