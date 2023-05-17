def hello_world() -> str:
    return "Здравствуй, мир!"


def lucky_sequence_1() -> tuple[int, int, int, int, int, int]:
    return 4, 8, 15, 16, 23, 42


def star_triangle() -> list[str]:
    return ["*" * i for i in range(1, 8)]


def greetings(name: str) -> str:
    return f"Привет, {name}"


def favorite_team(team_name: str) -> str:
    return f"{team_name} - чемпион!"


def repeat_after_me(list_words: list[str]) -> list[str]:
    return [word.replace("\n", "") for word in list_words]


def repeat_after_me_two(list_words: list[str]) -> list[str]:
    return [word.replace("\n", "") for word in reversed(list_words)]