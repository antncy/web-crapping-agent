import os
import chainlit as cl
import httpx

from chainlit.context import get_context
from urllib.parse import urlparse
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_base_url():
    try:
        context = get_context()
        referer = context.session.environ.get("HTTP_REFERER", "")
        parsed_url = urlparse(referer)  # Parse the referer URL
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    except Exception:
        port = 8000
        base_url = f"http://localhost:{port}"  # Default fallback URL
    return base_url

@cl.on_chat_start
def chat_start():
    cl.user_session.set(
        "history", 
        [{"role": "system", "content": "You are a helpful assistant."}]
    )


@cl.on_message
async def on_message(message: cl.Message):
    message_history = cl.user_session.get("history")
    message_history.append(
        {
            "role": "user",
            "content": message.content
        }
    )
    msg = cl.Message(content="")

    client = AsyncOpenAI(
        base_url="http://127.0.0.1:8000",
        api_key="sk-1234"
    )

    stream = await client.chat.completions.create(
        messages=message_history,
        model="string"
    )

    # async for part in stream:
    #     if token := part.choices[0].delta.content:
    #         await msg.stream_token(token)

    await cl.Message(stream).send()
    message_history.append(
        {
            "role": "assistant",
            "content": msg.content
        }
    )
    await msg.update()