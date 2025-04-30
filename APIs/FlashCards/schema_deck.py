from pydantic import BaseModel, Field
from schema_card import Card


class Deck(BaseModel):
    cards: list[Card] = Field(default_factory=list)
