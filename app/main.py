from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from app.schemas import PromptRequest, ResponseOutput
from app.logger import log_interaction
from app.model_handler import generate_response, generate_response_stream

app = FastAPI()

@app.post("/generate", response_model=ResponseOutput)
async def generate(request: PromptRequest):
    """
    Handle POST request to /generate endpoint.
    Generates a full response from the given prompt (non-streaming),
    logs the interaction, and returns the result as a JSON object.
    """
    response_text = generate_response(request.prompt)
    log_interaction(request.prompt, response_text)
    return {"response": response_text}


@app.post("/generate/stream")
async def generate_stream(request: PromptRequest):
    """
    Handle POST request to /generate/stream endpoint.
    Streams the response token-by-token from the model in real-time,
    logs the full interaction after streaming, and returns a streaming text response.
    """
    async def token_stream():
        full_response = ""
        async for token in generate_response_stream(request.prompt):
            full_response += token
            yield token
        log_interaction(request.prompt, full_response)

    return StreamingResponse(token_stream(), media_type="text/plain")
