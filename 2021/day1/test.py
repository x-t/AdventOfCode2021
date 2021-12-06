from unittest import TestCase

from part1 import day1part1
from part2 import day1part2


class TestDay1(TestCase):
    def test_day1part1(self):
        self.assertEqual(day1part1('test.txt'), 7)

    def test_day1part2(self):
        self.assertEqual(day1part2('test.txt'), 5)
