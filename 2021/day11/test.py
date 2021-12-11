from unittest import TestCase

from part1 import day11part1
from part2 import day11part2


class TestDay11(TestCase):
    def test_day11part1(self):
        self.assertEqual(day11part1('test.txt'), 1656)

    def test_day11part2(self):
        self.assertEqual(day11part2('test.txt'), 195)
