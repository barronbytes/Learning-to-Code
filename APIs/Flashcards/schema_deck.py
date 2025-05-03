from pydantic import BaseModel, Field
from schema_card import Card


class Deck(BaseModel):
    name_id: str
    cards: list[Card] = Field(default_factory=list)
