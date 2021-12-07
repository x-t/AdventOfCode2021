from unittest import TestCase

from part1 import day7part1
from part2 import day7part2


class TestDay7(TestCase):
    def test_day7part1(self):
        self.assertEqual(day7part1('test.txt'), 37)

    def test_day7part2(self):
        self.assertEqual(day7part2('test.txt'), 168)
