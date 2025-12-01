import aiohttp
import time
from colorama import Fore, Style, init
from openai import AsyncOpenAI
import asyncio
from functools import partial
init(autoreset=True)

# ==========================
# ⚙️ Função auxiliar (API HTTP)
# ==========================
async def ai_generate(model: str, prompt: str) -> str:
    """Chama o modelo do LM Studio via API HTTP local."""
    client = AsyncOpenAI(base_url="http://192.168.1.18:1234/v1", api_key="lm-studio")
    send_prompt = {"role": "system", "content": prompt}

    
    response = await client.chat.completions.create(
        model=model,
        messages=[send_prompt],
        temperature=0.7,
        stream=False,
    )
    return response.choices[0].message.content



# ==========================
# 🧩 Classe base
# ==========================
class AgenteBase:
    def __init__(self, modelo: str = "ollama-3.2"):
        self.modelo = modelo

    async def pensar(self, prompt: str) -> str:
        inicio = time.time()

        prompt = prompt + "\nResponda em Português."
        resposta = await ai_generate(self.modelo, prompt)

        return resposta

