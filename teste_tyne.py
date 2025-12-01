import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", dtype=torch.bfloat16, device_map="auto")


messages = [
    {
        "role": "system",
        "content": "Você é um chatbot amigável que sempre responde no estilo de um pirata. Responda em português.",
    },
    {
        "role": "user",
        "content": "Quantos helicópteros um ser humano consegue comer de uma vez?",
    },
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])