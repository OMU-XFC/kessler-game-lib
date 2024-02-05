import unittest

from src.kesslergame import Scenario

class TestAsteroidInit(unittest.TestCase):

    def test_only_number_passed(self):
        try:
            Scenario(num_asteroids=5)
            Scenario(num_asteroids=0)
        except ValueError:
            self.fail("Should not raise ValueError")

    def test_only_states_passed(self):
        try:
            Scenario(asteroid_states=[dict() for _ in range(5)])
            Scenario(asteroid_states=[])
        except ValueError:
            self.fail("Should not raise ValueError")

    def test_both_passed(self):
        with self.assertRaises(ValueError):
            Scenario(num_asteroids=50, asteroid_states=[dict() for _ in range(5)])

    def test_neither_passed(self):
        with self.assertRaises(ValueError):
            Scenario()


if __name__ == '__main__':
    unittest.main()
