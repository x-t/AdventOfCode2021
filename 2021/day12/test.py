from unittest import TestCase

from part1 import day12part1
from part2 import day12part2


class TestDay12(TestCase):
    def test_day12part1(self):
        self.assertEqual(day12part1('test.txt'), 10)
        self.assertEqual(day12part1('test_medium.txt'), 19)
        self.assertEqual(day12part1('test_large.txt'), 226)

    def test_day12part2(self):
        self.assertEqual(day12part2('test.txt'), 36)
        self.assertEqual(day12part2('test_medium.txt'), 103)
        self.assertEqual(day12part2('test_large.txt'), 3509)
