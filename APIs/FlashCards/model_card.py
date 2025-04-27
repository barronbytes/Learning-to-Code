from typing import Union
from pydantic import BaseModel


class Card(BaseModel):
    """ Single question-answer pair. """
    question: Union[str, int]
    answer: Union[str, int]
