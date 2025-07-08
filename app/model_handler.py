# Import Hugging Face's tokenizer and model for causal language modeling
from transformers import AutoTokenizer, AutoModelForCausalLM
# Import PyTorch for tensor manipulation
import torch
# Import asyncio for asynchronous token streaming
import asyncio

# Load the tokenizer and model for the "distilgpt2" model
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

# Function to generate a full response (non-streaming)
def generate_response(prompt: str, max_new_tokens=50) -> str:
    # Tokenize the prompt into input IDs
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    # Generate output tokens using top-k/top-p sampling
    output_ids = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        do_sample=True,           # Enable sampling instead of greedy decoding
        top_k=50,                 # Consider top 50 tokens for sampling
        top_p=0.95,               # Nucleus sampling: cumulative probability threshold
        temperature=0.9,          # Sampling temperature (creativity)
        eos_token_id=tokenizer.eos_token_id,  # End generation at EOS token
    )

    # Decode and return the full response as text
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Asynchronous generator for streaming token-by-token response
async def generate_response_stream(prompt: str, max_new_tokens=50):
    # Tokenize the input
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids

    # Generate tokens using the same sampling setting
