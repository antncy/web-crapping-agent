from fastapi import FastAPI, Request, Body, Depends
from fastapi.responses import JSONResponse, StreamingResponse
from src.main import llm_retrieve, llm_stream_history
from src.models.openai import OpenAIChatCompletionRequest

app = FastAPI()

def get_app_state(request: Request):
    return request.app.state.app_state

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/chat/completions")
async def retrieve_llm_response(query: str):
    response = await llm_retrieve(prompt=query)
    return {"response": response}

@app.post("/chat/completions")
async def chat_completions(
    request: OpenAIChatCompletionRequest = Body(...),
):
    response = llm_stream_history(request.messages)
    
    async def stream_response():
        async for chunk in response:
            yield chunk

    return StreamingResponse(stream_response())
