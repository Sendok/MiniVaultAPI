# Import Typer for building CLI applications
import typer
# Import requests for making HTTP requests
import requests

# Create a Typer app instance
app = typer.Typer()

# Base URL for the FastAPI backend
API_URL = "http://localhost:8000"

# CLI command to generate a full response from a prompt
@app.command()
def generate(prompt: str):
    """Generate a response from the prompt."""
    try:
        # Send a POST request to the /generate endpoint with the prompt
        r = requests.post(f"{API_URL}/generate", json={"prompt": prompt})
        r.raise_for_status()  # Raise error if response is not 200 OK
        response = r.json()["response"]
        typer.echo(f"\nResponse:\n{response}\n")  # Print the response to terminal
    except Exception as e:
        typer.echo(f"[ERROR] {e}")  # Handle any request or parsing errors

# CLI command to stream the response token-by-token
@app.command()
def stream(prompt: str):
    """Stream a response token-by-token."""
    try:
        # Send a POST request to the /generate/stream endpoint with streaming enabled
        r = requests.post(f"{API_URL}/generate/stream", json={"prompt": prompt}, stream=True)
        r.raise_for_status()  # Raise error if response is not successful
        typer.echo("\nStreaming response:\n")
        # Stream and print each chunk of the response as it arrives
        for chunk in r.iter_content(chunk_size=None):
            typer.echo(chunk.decode("utf-8"), nl=False)
    except Exception as e:
        typer.echo(f"[ERROR] {e}")  # Print error if something goes wrong

# Entry point when script is executed directly
if __name__ == "__main__":
    app()
