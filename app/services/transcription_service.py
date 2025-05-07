import whisper  # type: ignore
import tempfile


model = whisper.load_model("base")

def transcribe(audio_file):
    if audio_file is None:
        return ValueError("No audio file provided")
    
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        audio_file.save(tmp.name)
        transcription = model.transcribe(tmp.name)["text"]
    return transcription

