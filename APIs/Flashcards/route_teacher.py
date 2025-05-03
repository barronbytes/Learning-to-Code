from fastapi import APIRouter
from schema_deck import Deck
from service_deck import create_deck


router = APIRouter(prefix="/teacher", tags=["Teacher"])


# use plural nouns for resources
@router.post(path="/lessons", response_model=Deck)
def create_deck_route(name: str) -> Deck:
    return create_deck(name)
