from dataclasses import dataclass, asdict
import json

@dataclass
class LanguageResponse:
    language: str
    intent: str = "select_language"

    def to_json(self) -> str:
        """Convert the LanguageResponse object to a JSON string."""
        return json.dumps(asdict(self))
