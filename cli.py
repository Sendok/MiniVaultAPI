import typer
import requests

app = typer.Typer()

API_URL = "http://localhost:8000"

@app.command()
def generate(prompt: str):
    """
    Send a prompt to the /generate endpoint and print the full response.
    
    Args:
        prompt (str): The input text to send to the API.
    """
    try:
        r = requests.post(f"{API_URL}/generate", json={"prompt": prompt})
        r.raise_for_status()
        response = r.json()["response"]
        typer.echo(f"\nResponse:\n{response}\n")
    except Exception as e:
        typer.echo(f"[ERROR] {e}")

@app.command()
def stream(prompt: str):
    """
    Send a prompt to the /generate/stream endpoint and print the streamed response as it arrives.
    
    Args:
        prompt (str): The input text to send to the API for streaming.
    """
    try:
        r = requests.post(f"{API_URL}/generate/stream", json={"prompt": prompt}, stream=True)
        r.raise_for_status()
        typer.echo("\nStreaming response:\n")
        for chunk in r.iter_content(chunk_size=None):
            typer.echo(chunk.decode("utf-8"), nl=False)
    except Exception as e:
        typer.echo(f"[ERROR] {e}")

if __name__ == "__main__":
    app()
