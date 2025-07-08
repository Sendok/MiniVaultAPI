# Import JSON for writing log entries in JSON format
import json
# Import OS module to handle file and directory paths
import os
# Import datetime to timestamp log entries
from datetime import datetime

# Path to the JSONL log file
LOG_FILE = "logs/log.jsonl"

# Ensure the "logs" directory exists; create it if it doesn't
os.makedirs("logs", exist_ok=True)

# Function to log a prompt-response pair to a file
def log_interaction(prompt: str, response: str):
    # Create a log entry with current UTC timestamp, prompt, and response
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }

    # Append the log entry to the JSONL file (one JSON object per line)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
