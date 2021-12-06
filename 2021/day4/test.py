from unittest import TestCase

from part1 import day4part1
from part2 import day4part2


class TestDay4(TestCase):
    def test_day4part1(self):
        self.assertEqual(day4part1("test.txt"), 4512)

    def test_day4part2(self):
        self.assertEqual(day4part2("test.txt"), 1924)
