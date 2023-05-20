from itertools import permutations


def geometric_progression(b: int, q: int, n: int) -> int:
    assert isinstance(b, int)
    assert isinstance(q, int)
    assert isinstance(n, int)

    return b * q ** (n - 1)


def distance_in_meters(centimetre: int) -> int:
    assert isinstance(centimetre, int)

    return centimetre // 100


def mandarins(schoolboys: int, mandarins_count: int) -> tuple[int, int]:
    assert isinstance(schoolboys, int)
    assert isinstance(mandarins_count, int)

    return mandarins_count // schoolboys, mandarins_count % schoolboys


def inevitability(universe_population: int) -> int:
    assert isinstance(universe_population, int)

    return universe_population // 2 + universe_population % 2


def compartment_number(number: int) -> int:
    assert isinstance(number, int)

    return ((number - 1) // 4) + 1


def recalculating_time_interval(minutes_count: int) -> tuple[int, int]:
    assert isinstance(minutes_count, int)

    return minutes_count // 60, minutes_count % 60


def three_digit_number(number: int) -> tuple[int, int]:
    assert isinstance(number, int)
    assert (number > 0) == True

    a: int = number // 100 % 10
    b: int = number // 10 % 10
    c: int = number // 1 % 10

    return a + b + c, a * b * c


def permutation_of_digits(number: int) -> list[str]:
    assert isinstance(number, int)
    assert (99 < number < 1000) == True

    return ["".join(j) for j in [i for i in permutations(str(number))]]


def four_digit_number(number: int) -> tuple[int, int, int, int]:
    assert isinstance(number, int)
    assert (1000 <= number <= 9999) == True

    a: int = number // 1000 % 10
    b: int = number // 100 % 10
    c: int = number // 10 % 10
    d: int = number // 1 % 10

    return a, b, c, d
