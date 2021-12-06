from unittest import TestCase

from part1 import day3part1
from part2 import day3part2


class TestDay3(TestCase):
    def test_day3part1(self):
        self.assertEqual(day3part1('test.txt'), 198)

    def test_day3part2(self):
        self.assertEqual(day3part2('test.txt'), 230)
