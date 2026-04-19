from typing import Any, Dict

def parse_raw_data(raw: Dict[str, Any]) -> Dict[str, Any]:
    phrase = raw.get("phrase", "").strip()
    return {"phrase": phrase, "valid": bool(phrase)}