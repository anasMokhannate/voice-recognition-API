from flask import jsonify


def check_entities(json_response) :
    required = ["amount", "language", "operation_type", "operation"]
    missing = [e for e in required if e not in json_response]

    if missing:
        return {
            **json_response,
            "missing_entities": missing,
            "response": "Quel montant souhaitez-vous retirer ?" if "amount" in missing else ""
        }
    return json_response
    
    """
    Check the entities presence in the transcription.
    """

def get_file_from_request(request):

    if "file" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    return request.files["file"]
