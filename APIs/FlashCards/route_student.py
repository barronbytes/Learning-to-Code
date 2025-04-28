from fastapi import APIRouter
from model_deck import Deck
from service_deck import get_deck


router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/deck/{id}", response_model=Deck)
def get_deck_route(id: int) -> Deck:
    return get_deck(id)
