import unittest

from Source.Module_02.Lesson_02 import (
    hello_world,
    lucky_sequence_1,
    star_triangle,
    greetings,
    favorite_team,
    repeat_after_me,
    repeat_after_me_two
)


class TestLesson02(unittest.TestCase):
    @staticmethod
    def test_hello_world() -> None:
        assert hello_world() == "Здравствуй, мир!"

    @staticmethod
    def test_lucky_sequence_1() -> None:
        assert lucky_sequence_1() == (4, 8, 15, 16, 23, 42)

    @staticmethod
    def test_star_triangle() -> None:
        assert star_triangle() == ['*', '**', '***', '****', '*****', '******', '*******']

    @staticmethod
    def test_greetings() -> None:
        assert greetings("Тимур") == "Привет, Тимур"
        assert greetings("Гвидо") == "Привет, Гвидо"
        assert greetings("Питоняшка") == "Привет, Питоняшка"

    @staticmethod
    def test_favorite_team() -> None:
        assert favorite_team("ЦСКА") == "ЦСКА - чемпион!"
        assert favorite_team("Локомотив") == "Локомотив - чемпион!"
        assert favorite_team("Зенит") == "Зенит - чемпион!"

    @staticmethod
    def test_repeat_after_me() -> None:
        assert repeat_after_me(["I love", "Python", "so much"]) == ["I love", "Python", "so much"]
        assert repeat_after_me(["I used", "sys.stdin", "for this func"]) == ["I used", "sys.stdin", "for this func"]
        assert repeat_after_me(["I live", "in", "St.Petersburg"]) == ["I live", "in", "St.Petersburg"]

    @staticmethod
    def test_repeat_after_me_two() -> None:
        assert repeat_after_me_two(["I love", "Python", "so much"]) == ["so much", "Python", "I love"]
        assert repeat_after_me_two(["I used", "sys.stdin", "for this func"]) == ["for this func", "sys.stdin", "I used"]
        assert repeat_after_me_two(["I live", "in", "St.Petersburg"]) == ["St.Petersburg", "in", "I live"]


if __name__ == '__main__':
    unittest.main()
