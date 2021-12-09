from unittest import TestCase

from part1 import day9part1
from part2 import day9part2


class TestDay9(TestCase):
    def test_day9part1(self):
        self.assertEqual(day9part1("test.txt"), 15)

    def test_day9part2(self):
        self.assertEqual(day9part2("test.txt"), 1134)
