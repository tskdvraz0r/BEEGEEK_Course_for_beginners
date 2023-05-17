def i_like_python() -> list[str]:
    return ["I", "like", "Python"]


def custom_separator(list_words: list[str]) -> list[str]:
    return [word.replace("\n", "") for word in list_words]


def greetings(name: str) -> str:
    return f"Привет, {name}!"