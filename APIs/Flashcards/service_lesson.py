from schema_deck import Deck
from model_lesson import lessons


def create_lesson(name: str) -> dict[str, list]:
    lessons[name] = [] # modifying contents > NO NEED to use global keyword
    return {name: []}


def read_lessons() -> dict[str, Deck]:
    return lessons
