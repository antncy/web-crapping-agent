import os

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

model_settings = {
    "model":os.environ.get("MODEL_NAME"),
    "temperature": 0.2,
    "timeout": 60,
    "max_tokens": 1024
}

async def llm_retrieve(prompt: str, stream=False) -> str:
    client = AsyncOpenAI(api_key=os.environ.get("API_KEY"), base_url=os.environ.get("BASE_URL"))

    response = await client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        **model_settings,
        stream=stream
    )
    return response.choices[0].message.content

async def llm_stream_history(messages):
    client = AsyncOpenAI(api_key=os.environ.get("API_KEY"), base_url=os.environ.get("BASE_URL"))

    response = await client.chat.completions.create(
        messages=messages,
        **model_settings,
        stream=True
    )
    async for chunk in response:
        yield chunk.choices[0].delta.content

