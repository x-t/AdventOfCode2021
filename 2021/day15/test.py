from unittest import TestCase

from part1 import day15part1
from part2 import day15part2


class TestDay15(TestCase):
    def test_day15part1(self):
        self.assertEqual(day15part1('test.txt'), 40)

    def test_day15part2(self):
        self.assertEqual(day15part2('test.txt'), 315)
