from pydantic import BaseModel, Field


class Card(BaseModel):
    card_id: int
    question: str
    answer: str
