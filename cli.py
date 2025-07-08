import typer
import requests

app = typer.Typer()

API_URL = "http://localhost:8000"

@app.command()
def generate(prompt: str):
    """Generate a response from the prompt."""
    try:
        r = requests.post(f"{API_URL}/generate", json={"prompt": prompt})
        r.raise_for_status()
        response = r.json()["response"]
        typer.echo(f"\nResponse:\n{response}\n")
    except Exception as e:
        typer.echo(f"[ERROR] {e}")

@app.command()
def stream(prompt: str):
    """Stream a response token-by-token."""
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