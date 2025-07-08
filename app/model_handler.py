from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import asyncio

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilgpt2")

def generate_response(prompt: str, max_new_tokens=50) -> str:
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

    generated_ids = output_ids[0][input_ids.shape[1]:]  # only new tokens
    for token_id in generated_ids:
        token = tokenizer.decode(token_id, skip_special_tokens=True)
        await asyncio.sleep(0.05)  # Optional: delay simulated
        yield token
