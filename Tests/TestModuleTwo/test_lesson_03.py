import unittest

from Source.Module_02.Lesson_03 import i_like_python
from Source.Module_02.Lesson_03 import custom_separator
from Source.Module_02.Lesson_03 import greetings


class TestLesson03(unittest.TestCase):
    @staticmethod
    def test_i_like_python() -> None:
        assert i_like_python() == ["I", "like", "Python"]

    @staticmethod
    def test_custom_separator() -> None:
        assert custom_separator(["*", "Раз", "Два", "Три"]) == ["*", "Раз", "Два", "Три"]
        assert custom_separator(["##", "Money often", "costs", "too much"]) == ["##", "Money often", "costs",
                                                                                "too much"]
        assert custom_separator(["python", "1", "2", "3"]) == ["python", "1", "2", "3"]

    @staticmethod
    def test_greetings() -> None:
        assert greetings("Тирион") == "Привет, Тирион!"
        assert greetings("Джон") == "Привет, Джон!"
        assert greetings("Дейенерис") == "Привет, Дейенерис!"


if __name__ == '__main__':
    unittest.main()