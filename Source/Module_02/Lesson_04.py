def three_consecutive_numbers(number: int) -> tuple[int, int, int]:
    assert isinstance(number, int), "Ожидается целочисленное значение!"
    return number, number + 1, number + 2


def sum_three_numbers(list_numbers: list[int]) -> int:
    assert isinstance(list_numbers[0], int), "Значение должно быть целочисленным"
    assert isinstance(list_numbers[1], int), "Значение должно быть целочисленным"
    assert isinstance(list_numbers[2], int), "Значение должно быть целочисленным"

    return sum(list_numbers)


def cube(rib: int) -> tuple[int, int]:
    assert isinstance(rib, int), "Значение должно быть целочисленным"

    return rib ** 3, 6 * rib ** 2


def function_value(list_numbers: list[int]) -> None:
    assert isinstance(list_numbers[0], int), "Значение должно быть целочисленным"
    assert isinstance(list_numbers[1], int), "Значение должно быть целочисленным"

    a, b = list_numbers[0], list_numbers[1]

    return 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41


def next_and_previous(number: int) -> tuple[int, int, int]:
    assert isinstance(number, int), "Значение должно быть целочисленным"

    return number, number + 1, number - 1


def purchase_price(elements_costs: list[int]) -> int:
    assert isinstance(elements_costs[0], int), "Значение должно быть целочисленным"
    assert isinstance(elements_costs[1], int), "Значение должно быть целочисленным"
    assert isinstance(elements_costs[2], int), "Значение должно быть целочисленным"
    assert isinstance(elements_costs[3], int), "Значение должно быть целочисленным"

    return sum(elements_costs) * 3