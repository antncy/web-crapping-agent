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



async def llm_retrieve(prompt: str, history=[], stream=False) -> str:

    client = AsyncOpenAI(api_key=os.environ.get("API_KEY"), base_url=os.environ.get("BASE_URL"))
    
    history.append({
        "role": "user",
        "content": prompt
    })

    response = await client.chat.completions.create(
        messages=history,
        **model_settings,
        stream=stream
    )
    return response.choices[0].message.content
