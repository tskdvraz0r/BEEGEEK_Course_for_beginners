def password(pswrd: str, rpt_pswrd: str) -> str:
    assert isinstance(pswrd, str)
    assert isinstance(rpt_pswrd, str)

    return "Пароль принят" if pswrd == rpt_pswrd else "Пароль не принят"


def even_or_odd(number: int) -> str:
    assert isinstance(number, int)

    return "Четное" if number % 2 == 0 else "Нечетное"


def ratio(number: int) -> str:
    assert isinstance(number, int)

    a: int = number // 1000 % 10
    b: int = number // 100 % 10
    c: int = number // 10 % 10
    d: int = number // 1 % 10

    return "ДА" if (a + d) == (b - c) else "НЕТ"


def roskomnadzor(age: int) -> str:
    assert isinstance(age, int)

    return "Доступ разрешен" if age >= 18 else "Доступ запрещен"


def arithmetic_progression(a: int, b: int, c: int) -> str:
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(c, int)

    return "YES" if (abs(a - b)) == (abs(b - c)) else "NO"


def smallest_of_two_numbers(a: int, b: int) -> int:
    assert isinstance(a, int)
    assert isinstance(b, int)

    return min(a, b)


def smallest_of_four_numbers(a: int, b: int, c: int, d: int) -> int:
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(c, int)
    assert isinstance(d, int)

    return min(a, b, c, d)


def age_group(age: int) -> str:
    assert isinstance(age, int)

    if age <= 13:
        return "детство"

    elif 14 <= age <= 24:
        return "молодость"

    elif 25 <= age <= 59:
        return "зрелость"

    elif age >= 60:
        return "старость"


def only_plus(a: int, b: int, c: int) -> int:
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(c, int)

    sum_of_num: int = 0

    for num in [a, b, c]:
        if num > 0:
            sum_of_num += num

    return sum_of_num