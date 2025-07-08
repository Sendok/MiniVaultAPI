# Import TestClient to simulate requests to the FastAPI app
from fastapi.testclient import TestClient
# Import the FastAPI app
from app.main import app
# Import os for checking file existence
import os

# Create a test client for the FastAPI app
client = TestClient(app)

# Test the /generate endpoint (non-streaming)
def test_generate_stubbed_response():
    prompt = "Hello world"
    # Send POST request to the /generate endpoint with a prompt
    response = client.post("/generate", json={"prompt": prompt})
    assert response.status_code == 200  # Ensure the request was successful
    json_data = response.json()
    assert "response" in json_data  # Response must contain the "response" key
    assert prompt in json_data["response"]  # The generated text should include the prompt

# Test the /generate/stream endpoint (streaming response)
def test_generate_streaming_response():
    prompt = "Once upon a time"
    # Send POST request to the streaming endpoint
    response = client.post("/generate/stream", json={"prompt": prompt})
    assert response.status_code == 200  # Ensure success
    assert response.headers["content-type"].startswith("text/plain")  # Confirm streaming format

    content = ""
    # Read streamed content chunk-by-chunk
    for chunk in response.iter_text():
        content += chunk

    # Ensure some content was actually generated
    assert len(content.strip()) > 0
    # Optionally, check that at least 3 words were generated
    assert len(content.split()) >= 3

# Test that the log file has been written
def test_log_file_written():
    # Check that the log file exists
    assert os.path.exists("logs/log.jsonl")
    # Open the log file and read lines
    with open("logs/log.jsonl") as f:
        lines = f.readlines()
    # Ensure at least one log entry is present
    assert len(lines) > 0
