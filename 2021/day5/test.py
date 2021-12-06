from unittest import TestCase

from part1 import day5part1
from part2 import day5part2


class TestDay5(TestCase):
    def test_day5part1(self):
        self.assertEqual(day5part1('test.txt'), 5)

    def test_day5part2(self):
        self.assertEqual(day5part2('test.txt'), 12)
