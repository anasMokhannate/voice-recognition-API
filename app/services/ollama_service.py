import requests
import os
from flask import jsonify, logging

# think about adjusting temperature 

OLLAMA_URL = os.getenv("OLLAMA_URL")  # updated endpoint
OLLAMA_MODEL = "gemma3:1b"


def sendLanguageRequest(prompt): 
    ollama_payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "format": {
            "type": "object",
            "properties": {
                "intent": {
                    "type": "String"
                },
                "language": {
                    "type": "String"
                }
            },
            "required": [
                "intent",
                "language"
            ]
        },
        "stream": False,
        "options": {
            "temperature": 0.8,
        },
    }

    try:
        response = requests.post(OLLAMA_URL + "/api/chat", json=ollama_payload)
        logging.info(f"request sent to ollama: {str(ollama_payload)}")
        logging.info(f"Response : {str(response.text)}")
        logging.info(f"Response : {str(response.status_code)}")
        response.raise_for_status()
        data = response.json()
        
        model_reply = data.get("message", {}).get("content", "")
    except requests.RequestException as e:
        return jsonify({"error": "Ollama request failed", "details": str(e)}), 500
    except ValueError:
        return jsonify({"error": "Invalid JSON returned from Ollama"}), 500

    return jsonify({
        "transcription": prompt,
        "ollama_response": jsonify(model_reply)
    })

def sendOperationRequest(prompt): 
    ollama_payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
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


def sendOperationTypeRequest(prompt): 
    ollama_payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "format": {
            "type": "object",
            "properties": {
                "operationType": {
                    "type": "String"
                }
            },
            "required": [
                "operationType",
            ]
        },
        "stream": False,
        "options": {
            "temperature": 0.8,
        },
    }

    try:
        response = requests.post(OLLAMA_URL + "/api/chat", json=ollama_payload)
        logging.info(f"Response : {str(response.text)}")
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

def send_amount(prompt):
    ollama_payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "format": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "number"
                }
            },
            "required": [
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