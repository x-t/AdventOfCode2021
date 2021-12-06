from unittest import TestCase

from part1 import day2part1
from part2 import day2part2


class TestDay2(TestCase):
    def test_day2part1(self):
        self.assertEqual(day2part1('test.txt'), 150)

    def test_day2part2(self):
        self.assertEqual(day2part2('test.txt'), 900)
