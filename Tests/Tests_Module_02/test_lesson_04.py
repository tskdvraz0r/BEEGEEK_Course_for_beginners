import unittest

from Source.Module_02.Lesson_04 import *


class TestLesson04(unittest.TestCase):
    @staticmethod
    def test_three_consecutive_numbers() -> None:
        assert three_consecutive_numbers(8) == (8, 9, 10)
        assert three_consecutive_numbers(-341) == (-341, -340, -339)
        assert three_consecutive_numbers(-1) == (-1, 0, 1)

    @staticmethod
    def test_sum_three_numbers() -> None:
        assert sum_three_numbers([9, 11, 2]) == 22
        assert sum_three_numbers([-1, 10, 1]) == 10
        assert sum_three_numbers([-7, -10, -3]) == -20

    @staticmethod
    def test_cube() -> None:
        assert cube(25) == (15625, 3750)
        assert cube(13) == (2197, 1014)
        assert cube(56) == (175616, 18816)

    @staticmethod
    def test_function_value() -> None:
        assert function_value([1, 1]) == 131
        assert function_value([1, 0]) == -165
        assert function_value([0, 1]) == 237

    @staticmethod
    def test_next_and_previous() -> None:
        assert next_and_previous(3) == (3, 4, 2)
        assert next_and_previous(15) == (15, 16, 14)
        assert next_and_previous(-41) == (-41, -40, -42)

    @staticmethod
    def test_purchase_price() -> None:
        assert purchase_price([9900, 55600, 3999, 2990]) == 217467
        assert purchase_price([15700, 80550, 12050, 5890]) == 342570
        assert purchase_price([44990, 123300, 19600, 8990]) == 590640

    @staticmethod
    def test_arithmetic_operations() -> None:
        assert arithmetic_operations([1, 2]) == (3, -1, 2)
        assert arithmetic_operations([7, 16]) == (23, -9, 112)
        assert arithmetic_operations([10, 10]) == (20, 0, 100)

    @staticmethod
    def test_arithmetic_progression() -> None:
        assert arithmetic_progression(1, 1, 10) == 10
        assert arithmetic_progression(-1, 1, 2) == 0
        assert arithmetic_progression(100, 50, 1) == 100

    @staticmethod
    def test_divide_and_conquer() -> None:
        assert divide_and_conquer(3) == [3, 6, 9, 12, 15]
        assert divide_and_conquer(13) == [13, 26, 39, 52, 65]
        assert divide_and_conquer(23) == [23, 46, 69, 92, 115]


if __name__ == '__main__':
    unittest.main()
