from schema_deck import Deck
from model_database import db


def create_deck(name: str) -> Deck:
    deck = Deck(deck_id=name, cards=[])
    db[name] = deck
    return deck


def read_deck(name: str) -> Deck:
    pass
