from pydantic import BaseModel, Field
from schema_card import Card


class Lesson(BaseModel):
    id: int
    cards: list[Card] = Field(default_factory=list)
