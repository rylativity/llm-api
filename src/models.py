from pydantic import BaseModel

class LlmRequest(BaseModel):
    inputs: dict
    prompt_template:str | None = None
    generation_kwargs:dict | None = None
    
