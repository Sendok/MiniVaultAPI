# Import BaseModel from Pydantic to define data validation models
from pydantic import BaseModel

# Request model: defines the expected structure of input data
class PromptRequest(BaseModel):
    prompt: str  # The user's input prompt to the language model

# Response model: defines the structure of the API's JSON response
class ResponseOutput(BaseModel):
    response: str  # The generated text returned by the model
