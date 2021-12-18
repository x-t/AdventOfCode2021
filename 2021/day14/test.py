from unittest import TestCase

from part1 import day14part1
from part2 import day14part2


class TestDay14(TestCase):
    def test_day14part1(self):
        self.assertEqual(day14part1('test.txt'), 1588)

    def test_day14part2(self):
        self.assertEqual(day14part2('test.txt'), 2188189693529)
