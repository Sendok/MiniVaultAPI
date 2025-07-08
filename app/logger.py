import json
import os
from datetime import datetime

LOG_FILE = "logs/log.jsonl"
os.makedirs("logs", exist_ok=True)

def log_interaction(prompt: str, response: str):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
