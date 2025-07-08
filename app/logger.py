import json
import os
from datetime import datetime

# Path to the JSONL log file
LOG_FILE = "logs/log.jsonl"

# Ensure the "logs" directory exists; create it if it doesn't
os.makedirs("logs", exist_ok=True)

def log_interaction(prompt: str, response: str):
    """
    Log a prompt-response interaction to a JSONL file with a UTC timestamp.
    
    Args:
        prompt (str): The input prompt sent to the model.
        response (str): The model's generated response.
    
    Each log entry is stored as a single JSON object per line in the log file.
    Useful for audit logging, analytics, or debugging.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
