def star_rectangle() -> list[str]:

    return [
        "*" * 17,
        "*" + " " * 15 + "*",
        "*" + " " * 15 + "*",
        "*" * 17
    ]


def sum_of_square_vs_square_of_sum(a: int, b: int) -> tuple[int, int]:
    assert isinstance(a, int)
    assert isinstance(b, int)

    return (a + b) ** 2, a ** 2 + b ** 2


def big_number(a: int, b: int, c: int, d: int) -> None:
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(c, int)
    assert isinstance(d, int)

    return a ** b + c ** d


def reproduction_number(number: int) -> int:
    assert isinstance(number, int)

    return number + int(str(number) * 2) + int(str(number) * 3)