from unittest import TestCase

from part1 import day8part1
from part2 import day8part2


class TestDay8(TestCase):
    def test_day8part1(self):
        self.assertEqual(day8part1('test.txt'), 26)

    def test_day8part2(self):
        self.assertEqual(day8part2('test.txt'), 61229)
