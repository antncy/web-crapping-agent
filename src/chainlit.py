import os
import chainlit as cl
from main import llm_retrieve


@cl.on_chat_start
def chat_start():
    cl.user_session.set(
        "history", 
        [{"role": "system", "content": "You are a helpful assistant."}]
    )


@cl.on_message
async def on_message(message: cl.Message):
    message_history = cl.user_session.get("history")

    msg = cl.Message(content="")
    stream = await llm_retrieve(prompt=message.content, history=message_history, stream=True)

    async for part in stream:
        if token := part.choices[0].delta.content:
            await msg.stream_token(token)
    message_history.extend(
        {
            "role": "user",
            "content": message.content
        },
        {
            "role": "assistant",
            "content": msg.content
        }
    )
    await msg.update()