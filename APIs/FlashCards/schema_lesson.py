from pydantic import BaseModel
from schema_card import Card


class Lesson(BaseModel):
    id: int
    cards: list[Card]
