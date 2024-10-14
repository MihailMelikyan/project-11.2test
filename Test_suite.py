import unittest

import runner_test
import test

tournament_testST = unittest.TestSuite()
tournament_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(test.TournamentTest))
tournament_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournament_testST)
