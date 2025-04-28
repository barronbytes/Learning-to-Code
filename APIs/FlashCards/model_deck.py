from pydantic import BaseModel, Field
from model_card import Card


class Deck(BaseModel):
    """ Collection of flash cards by class. """
    id: int
    name: str
    pairs: list[Card] = Field(default_factory=list)