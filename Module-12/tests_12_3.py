import unittest


def freeze_test(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        return func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False  # атрибут, определяющий заморожен тест или нет

    @freeze_test
    def test_run(self):
        self.assertEqual(1 + 1, 2)

    @freeze_test
    def test_walk(self):
        self.assertEqual(2 * 2, 4)

    @freeze_test
    def test_challenge(self):
        self.assertEqual(3 - 1, 2)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @freeze_test
    def test_first_tournament(self):
        self.assertTrue(True)

    @freeze_test
    def test_second_tournament(self):
        self.assertFalse(False)

    @freeze_test
    def test_third_tournament(self):
        self.assertEqual("test".upper(), "TEST")
