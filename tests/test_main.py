from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_generate_stubbed_response():
    """
    Test the /generate endpoint.
    Verifies that a response is returned and contains the original prompt.
    """
    prompt = "Hello world"
    response = client.post("/generate", json={"prompt": prompt})
    assert response.status_code == 200
    json_data = response.json()
    assert "response" in json_data
    assert prompt in json_data["response"]

def test_generate_streaming_response():
    """
    Test the /generate/stream endpoint.
    Verifies that streaming response works, has correct content type,
    and yields non-empty output with at least a few words.
    """
    prompt = "Once upon a time"
    response = client.post("/generate/stream", json={"prompt": prompt})
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")

    content = ""
    for chunk in response.iter_text():
        content += chunk

    # Ensure the response is not empty
    assert len(content.strip()) > 0
    # Optionally check for a minimum word count
    assert len(content.split()) >= 3

def test_log_file_written():
    """
    Test whether the log file exists and has at least one log entry.
    Verifies logging functionality is working after generation endpoints are hit.
    """
    assert os.path.exists("logs/log.jsonl")
    with open("logs/log.jsonl") as f:
        lines = f.readlines()
    assert len(lines) > 0
