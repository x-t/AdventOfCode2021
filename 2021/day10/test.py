from unittest import TestCase

from part1 import day10part1
from part2 import day10part2


class TestDay10(TestCase):
    def test_day10part1(self):
        self.assertEqual(day10part1('test.txt'), 26397)

    def test_day10part2(self):
        self.assertEqual(day10part2('test.txt'), 288957)
