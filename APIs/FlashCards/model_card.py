from typing import Union
from pydantic import BaseModel, Field


class Card(BaseModel):
    """ Single question-answer pair. """
    question: Union[str, int]
    answer: Union[str, int]
    tags: list[str] = Field(default_factory=list)
