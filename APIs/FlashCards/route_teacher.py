from fastapi import APIRouter
from schema_lesson import Lesson
from service_lesson import read_lesson


router = APIRouter(prefix="/teacher", tags=["Teacher"])


@router.get(path="/lesson/{id}", response_model=Lesson)
def read_lesson_route(id: int) -> Lesson:
    return read_lesson(id)
