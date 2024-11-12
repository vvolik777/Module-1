import unittest
import logging
from runner import Runner

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                    format='%(levelname)s: %(message)s')  # настраиваем логирование


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Тестовый бегун", speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(123, speed=5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    unittest.main()