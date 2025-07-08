# Import FastAPI framework and StreamingResponse for streaming output
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

# Import data models and response schema
from app.schemas import PromptRequest, ResponseOutput
# Import function to log interactions
from app.logger import log_interaction
# Import functions to handle generation (standard and streaming)
from app.model_handler import generate_response, generate_response_stream

# Create a FastAPI app instance
app = FastAPI()

# Endpoint to handle non-streaming text generation
@app.post("/generate", response_model=ResponseOutput)
async def generate(request: PromptRequest):
    # Generate the full response from the prompt
    response_text = generate_response(request.prompt)
    
    # Log the prompt and generated response
    log_interaction(request.prompt, response_text)

    # Return the response in JSON format
    return {"response": response_text}

# Endpoint to handle streaming text generation
@app.post("/generate/stream")
async def generate_stream(request: PromptRequest):
    # Define an async generator function to yield tokens as they're generated
    async def token_stream():
        full_response = ""
        async for token in generate_response_stream(request.prompt):
            full_response += token
            yield token  # Send each token to the client as it's ready
        
        # Log the full response after streaming is complete
        log_interaction(request.prompt, full_response)

    # Return a streaming response to the client (plain text)
    return StreamingResponse(token_stream(), media_type="text/plain")
