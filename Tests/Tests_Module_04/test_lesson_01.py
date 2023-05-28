import unittest

from Source.Module_04.Lesson_01 import *


class TestLesson01(unittest.TestCase):
    @staticmethod
    def test_password() -> None:
        assert password("qwerty", "qwerty") == "Пароль принят"
        assert password("qwerty", "Qwerty") == "Пароль не принят"
        assert password("PythonROCKS", "PythonROCKS") == "Пароль принят"
        assert password("123456789", "12345678") == "Пароль не принят"
        assert password("Python2", "Python3") == "Пароль не принят"

    @staticmethod
    def test_even_or_odd() -> None:
        assert even_or_odd(10) == "Четное"
        assert even_or_odd(17) == "Нечетное"
        assert even_or_odd(0) == "Четное"
        assert even_or_odd(-19) == "Нечетное"
        assert even_or_odd(1) == "Нечетное"

    @staticmethod
    def test_ratio() -> None:
        assert ratio(1614) == "ДА"
        assert ratio(1234) == "НЕТ"
        assert ratio(7911) == "ДА"
        assert ratio(9248) == "НЕТ"
        assert ratio(4840) == "ДА"

    @staticmethod
    def test_roskomnadzor() -> None:
        assert roskomnadzor(16) == "Доступ запрещен"
        assert roskomnadzor(18) == "Доступ разрешен"
        assert roskomnadzor(19) == "Доступ разрешен"
        assert roskomnadzor(35) == "Доступ разрешен"
        assert roskomnadzor(7) == "Доступ запрещен"

    @staticmethod
    def test_arithmetic_progression() -> None:
        assert arithmetic_progression(1, 2, 3) == "YES"
        assert arithmetic_progression(1, 2, 4) == "NO"
        assert arithmetic_progression(2, 4, 8) == "NO"
        assert arithmetic_progression(10, 5, 0) == "YES"
        assert arithmetic_progression(25, 125, 224) == "NO"

    @staticmethod
    def test_smallest_of_two_numbers() -> None:
        assert smallest_of_two_numbers(8, 11) == 8
        assert smallest_of_two_numbers(20, 5) == 5
        assert smallest_of_two_numbers(-12, -21) == -21
        assert smallest_of_two_numbers(-100, 2) == -100
        assert smallest_of_two_numbers(0, 100) == 0

    @staticmethod
    def test_smallest_of_four_numbers() -> None:
        assert smallest_of_four_numbers(1, 2, 3, 4) == 1
        assert smallest_of_four_numbers(10, 9, 11, 12) == 9
        assert smallest_of_four_numbers(100, 200, 5, 300) == 5
        assert smallest_of_four_numbers(2, 2, 3, 4) == 2
        assert smallest_of_four_numbers(67, 8, 8, 89) == 8

    @staticmethod
    def test_age_group() -> None:
        assert age_group(4) == "детство"
        assert age_group(91) == "старость"
        assert age_group(40) == "зрелость"
        assert age_group(19) == "молодость"
        assert age_group(25) == "зрелость"

    @staticmethod
    def test_only_plus() -> None:
        assert only_plus(4, -22, 1) == 5
        assert only_plus(33, 55, 63) == 151
        assert only_plus(-1, 37, 62) == 99
        assert only_plus(-31, -11, 5) == 5
        assert only_plus(-4, -7, -18) == 0


if __name__ == '__main__':
    unittest.main()
