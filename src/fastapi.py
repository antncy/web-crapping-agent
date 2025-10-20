from typing import Union

from fastapi import FastAPI
from src.main import llm_retrieve

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/retrieve")
async def retrieve_llm_response(query: str):
    response = await llm_retrieve(prompt=query)
    print(response)
    return {"response": response}
