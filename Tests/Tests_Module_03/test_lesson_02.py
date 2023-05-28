import unittest

from Source.Module_03.Lesson_02 import *


class TestLesson02(unittest.TestCase):
    @staticmethod
    def test_star_rectangle() -> None:
        assert star_rectangle() == ['*****************', '*               *', '*               *', '*****************']

    @staticmethod
    def test_sum_of_square_vs_square_of_sum() -> None:
        assert sum_of_square_vs_square_of_sum(3, 2) == (25, 13)
        assert sum_of_square_vs_square_of_sum(-5, 1) == (16, 26)
        assert sum_of_square_vs_square_of_sum(17, 0) == (289, 289)
        assert sum_of_square_vs_square_of_sum(0, 25) == (625, 625)
        assert sum_of_square_vs_square_of_sum(10, 10) == (400, 200)

    @staticmethod
    def test_big_number() -> None:
        assert big_number(9, 29, 7, 27) == 4710194409608608369201743232
        assert big_number(2, 3, 2, 5) == 40
        assert big_number(1, 1, 1, 1) == 2
        assert big_number(7, 8, 9, 10) == 3492549202
        assert big_number(50, 5, 100, 30) == 1000000000000000000000000000000000000000000000000000312500000

    @staticmethod
    def test_reproduction_number() -> None:
        assert reproduction_number(1) == 123
        assert reproduction_number(3) == 369
        assert reproduction_number(5) == 615
        assert reproduction_number(7) == 861
        assert reproduction_number(9) == 1107


if __name__ == '__main__':
    unittest.main()
