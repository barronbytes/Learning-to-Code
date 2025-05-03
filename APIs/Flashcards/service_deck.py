from schema_deck import Deck
from model_database import db


def create_lesson(name: str) -> Deck:
    deck = Deck(name, {})
    db[name] = {}
    return deck


def read_lesson(name: str) -> Deck:
    pass
