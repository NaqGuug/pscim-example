import json
from pathlib import Path
from typing import Any

FULL_USER_JSON: str = (Path(__file__).parent / "full_user.json").read_text()
FULL_USER: dict[str, Any] = json.loads(FULL_USER_JSON)
