from schema_lesson import Lesson
from model_flashcards import lesson_id, flashcards


def create_lesson() -> Lesson:
    global lesson_id # reassigning value > MUST use global keyword
    new_lesson = Lesson(id=lesson_id)
    flashcards[lesson_id] = new_lesson # modifying contents > NO NEED to use global keyword
    lesson_id += 1
    return new_lesson


def read_lesson(id: int) -> Lesson:
    return flashcards[id]
