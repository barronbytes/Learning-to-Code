from fastapi import APIRouter
from schema_deck import Deck
from service_deck import create_deck, read_deck


router = APIRouter(prefix="/teacher", tags=["Teacher"])


# use plural nouns for resources
@router.post(path="/decks", response_model=Deck)
def create_deck_route(name: str) -> Deck:
    return create_deck(name)


@router.get(path="/decks/{name}", response_model=Deck)
def read_deck_route(name: str) -> Deck:
    return read_deck(name)
