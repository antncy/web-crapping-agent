import os
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model_settings = {
    "model":os.getenv("MODEL_NAME"),
    "base_url":os.environ.get("BASE_URL"),
    "api_key":os.environ.get("API_KEY"),
    "temperature": 0.2,
    "timeout": 60,
    "max_tokens": 1024
}

async def llm_retrieve(prompt: str, history=[], stream=False) -> str:

    llm = ChatOpenAI(**model_settings).with_retry(stop_after_attempt=2)
    history.append({
        "role": "user",
        "content": prompt
    })

    message = HumanMessage(content=history)
    response = await llm.ainvoke([message], stream=stream)
    return response
