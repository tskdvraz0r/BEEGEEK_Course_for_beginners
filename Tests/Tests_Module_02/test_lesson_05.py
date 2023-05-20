import unittest

from Source.Module_02.Lesson_05 import *


class TestLesson05(unittest.TestCase):
    @staticmethod
    def test_geometric_progression() -> None:
        assert geometric_progression(1, 2, 5) == 16
        assert geometric_progression(10, -2, 6) == -320
        assert geometric_progression(-2, 10, 3) == -200
        assert geometric_progression(1, 1, 100001) == 1
        assert geometric_progression(15, -3, 5) == 1215

    @staticmethod
    def test_distance_in_meters() -> None:
        assert distance_in_meters(345) == 3
        assert distance_in_meters(100) == 1
        assert distance_in_meters(89) == 0
        assert distance_in_meters(9_330) == 93
        assert distance_in_meters(4_421_345) == 44_213

    @staticmethod
    def test_mandarins() -> None:
        assert mandarins(3, 6) == (2, 0)
        assert mandarins(12, 6) == (0, 6)
        assert mandarins(7, 4) == (0, 4)
        assert mandarins(5, 60) == (12, 0)
        assert mandarins(6, 6) == (1, 0)

    @staticmethod
    def test_inevitability() -> None:
        assert inevitability(99) == 50
        assert inevitability(1_132) == 566
        assert inevitability(1) == 1
        assert inevitability(2) == 1
        assert inevitability(124_234_413_532) == 62_117_206_766

    @staticmethod
    def test_compartment_number() -> None:
        assert compartment_number(1) == 1
        assert compartment_number(5) == 2
        assert compartment_number(9) == 3
        assert compartment_number(13) == 4
        assert compartment_number(17) == 5
        assert compartment_number(21) == 6
        assert compartment_number(25) == 7
        assert compartment_number(29) == 8
        assert compartment_number(33) == 9

    @staticmethod
    def test_recalculating_time_interval() -> None:
        assert recalculating_time_interval(150) == (2, 30)
        assert recalculating_time_interval(50) == (0, 50)
        assert recalculating_time_interval(240) == (4, 0)
        assert recalculating_time_interval(400) == (6, 40)
        assert recalculating_time_interval(90) == (1, 30)

    @staticmethod
    def test_three_digit_number() -> None:
        assert three_digit_number(123) == (6, 6)
        assert three_digit_number(333) == (9, 27)
        assert three_digit_number(101) == (2, 0)
        assert three_digit_number(100) == (1, 0)
        assert three_digit_number(999) == (27, 729)

    @staticmethod
    def test_permutation_of_digits() -> None:
        assert permutation_of_digits(123) == ["123", "132", "213", "231", "312", "321"]
        assert permutation_of_digits(987) == ["987", "978", "897", "879", "798", "789"]
        assert permutation_of_digits(658) == ["658", "685", "568", "586", "865", "856"]

    @staticmethod
    def test_four_digit_number() -> None:
        assert four_digit_number(3281) == (3, 2, 8, 1)
        assert four_digit_number(1000) == (1, 0, 0, 0)
        assert four_digit_number(9999) == (9, 9, 9, 9)
        assert four_digit_number(7564) == (7, 5, 6, 4)
        assert four_digit_number(9080) == (9, 0, 8, 0)


if __name__ == '__main__':
    unittest.main()
