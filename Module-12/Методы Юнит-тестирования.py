import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in list(self.participants):
                participant.run()

            for participant in list(self.participants):
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # словарь для сохранения результатов всех тестов

    def setUp(self):
        self.runner_usain = Runner("Usain", speed=10)
        self.runner_andrey = Runner("Andrey", speed=9)
        self.runner_nik = Runner("Nik", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")

    def test_race_usain_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        result = tournament.start()

        self.__class__.all_results["Usain and Nik"] = {place: str(runner) for place, runner in result.items()}
        last_place_runner = result[max(result.keys())]
        self.assertTrue(last_place_runner == "Nik")

    def test_race_andrey_nik(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nik)
        result = tournament.start()

        self.__class__.all_results["Andrey and Nik"] = {place: str(runner) for place, runner in result.items()}
        last_place_runner = result[max(result.keys())]
        self.assertTrue(last_place_runner == "Nik")

    def test_race_usain_andrey_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
        result = tournament.start()
        self.__class__.all_results["Usain, Andrey and Nik"] = {place: str(runner) for place, runner in result.items()}
        last_place_runner = result[max(result.keys())]
        self.assertTrue(last_place_runner == "Nik")

    def test_all_runners_finish_in_order_of_speed(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nik)
        result = tournament.start()

        expected_order = ["Usain", "Andrey", "Nik"]
        actual_order = [str(result[place]) for place in sorted(result.keys())]
        self.assertEqual(actual_order, expected_order)

    def test_short_distance_race(self):
        tournament = Tournament(20, self.runner_usain, self.runner_andrey, self.runner_nik)
        result = tournament.start()

        first_place_runner = result[1]
        self.assertTrue(first_place_runner == "Usain")


if __name__ == "__main__":
    unittest.main()
