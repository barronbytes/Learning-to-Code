from fastapi import APIRouter, HTTPException
from service_deck import get_deck  # Import the get_deck function from service_deck.py
from model_deck import Deck


router = APIRouter(prefix="/student", tags=["Student"])


@router.get("/deck/{id}", response_model=Deck)
def get_deck_route(id: int) -> Deck:
    return get_deck(id)
