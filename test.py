from runner_and_tournament import *
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, result in enumerate(cls.all_results):
            formated_result = {key: runner.name for key, runner in result.items()}
            print(f'{i + 1}. {formated_result}')
    @unittest.skipIf(True,'Тесты в этом кейсе заморожены')
    def test_first_tournament(self):
        tournament = Tournament(90, self.run1, self.run3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_second_tournament(self):
        tournament = Tournament(90, self.run2, self.run3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[2] == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_third_tournament(self):
        tournament = Tournament(90, self.run1, self.run2, self.run3)
        results = tournament.start()
        TournamentTest.all_results.append(results)
        self.assertTrue(results[3] == 'Ник')
