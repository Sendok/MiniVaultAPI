from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class ResponseOutput(BaseModel):
    response: str
