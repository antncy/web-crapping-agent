import os
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

model_settings = {
    "model": os.getenv("MODEL_NAME"),
    "base_url": os.getenv("BASE_URL"),
    "api_key": os.getenv("API_KEY"),
    "temperature": 0.2,
    "max_retries": 3,
    "timeout": 60,
}

def llm_retrieve(prompt: str) -> str:

    llm = ChatOpenAI(**model_settings).with_retry(stop_after_attempt=2)
    message = HumanMessage(
            content=[
                {"type": "text", "text": prompt},
            ]
        )

    response = llm.invoke([message])
    return response.content
