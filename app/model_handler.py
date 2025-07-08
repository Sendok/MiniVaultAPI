from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import asyncio

# Load the tokenizer and model from Hugging Face (DistilGPT2 in this case)
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

def generate_response(prompt: str, max_new_tokens=50) -> str:
    """
    Generate a full text response from a given prompt using a causal language model.
    
    Args:
        prompt (str): The input text prompt.
        max_new_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: The generated response text.
    """
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output_ids = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9,
        eos_token_id=tokenizer.eos_token_id,
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

async def generate_response_stream(prompt: str, max_new_tokens=50):
    """
    Asynchronously generate a text response from a prompt, yielding tokens one at a time.
    Useful for streaming output in real time.
    
    Args:
        prompt (str): The input text prompt.
        max_new_tokens (int): Maximum number of tokens to generate.

    Yields:
        str: The next decoded token in the generated response.
    """
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    output_ids = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.9,
        eos_token_id=tokenizer.eos_token_id,
    )

    generated_ids = output_ids[0][input_ids.shape[1]:]  # Only return new tokens
    for token_id in generated_ids:
        token = tokenizer.decode(token_id, skip_special_tokens=True)
        await asyncio.sleep(0.05)  # Optional: simulate delay for streaming effect
        yield token
