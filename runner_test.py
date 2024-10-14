from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    @unittest.skipIf(False,'')
    def test_walk(self):
        r1 = Runner('Harry')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(False,'')
    def test_run(self):
        r2 = Runner('Thomas')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(False,'')
    def test_challenge(self):
        r1 = Runner('Harry')
        r2 = Runner('Thomas')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__test__':
    unittest.main()
