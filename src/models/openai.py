from typing import Any, Dict, List, Literal, Optional, Union
from pydantic import BaseModel, Field

class OpenAIMessage(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class OpenAIChatCompletionRequest(BaseModel):
    model: str = Field(..., description="model name")
    messages: List[OpenAIMessage]
    temperature: Optional[float] = Field(0.3)
    top_p: Optional[float] = Field(1.0)
    stream: Optional[bool] = Field(False)
    max_tokens: Optional[int] = Field(1024)
    logprobs: Optional[int] = Field(None)