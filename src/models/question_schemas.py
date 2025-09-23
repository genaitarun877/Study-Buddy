from typing import List
from pydantic import BaseModel, Field,validator


class MCQQuestion(BaseModel):
    question:str = Field(..., description="The question to be asked")
    options:List[str] = Field(..., description="The options for the question")
    correct_answer:str = Field(..., description="The correct answer to the question")

    @validator('question',pre=True)
    def clean_question(cls, v):
        if isinstance(v,dict):
            return v.get('description',str(v))
        return str(v)

class FillBlankQuestion(BaseModel):
    question: str = Field(..., description="The question text with '___' for the blank  ")
    answer: str = Field(..., description="The correct word or the phrse for the blank")    
    
    @validator('question',pre=True)
    def clean_question(cls, v):
        if isinstance(v,dict):
            return v.get('description',str(v))
        return str(v)

    