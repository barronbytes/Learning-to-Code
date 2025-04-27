from pydantic import BaseModel
from model_card import Card


class Lesson(BaseModel):
    """ Lesson objective tags, question-answer pairs, and unique id.  """
    tags: list[str]
    questions: list[Card]
    lesson_id: int
