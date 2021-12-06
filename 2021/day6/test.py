from unittest import TestCase

from part1 import day6part1
from part2 import day6part2


class TestDay6(TestCase):
    def test_day6part1(self):
        self.assertEqual(day6part1('test.txt'), 5934)

    def test_day6part2(self):
        self.assertEqual(day6part2('test.txt'), 26984457539)
