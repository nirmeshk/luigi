from hypothesis import given, assume
from hypothesis.strategies import text, integers

import unittest
import math
from luigi import luigi_math


class TestLuigiMath(unittest.TestCase):
    @given(integers())
    def test_inc(self, a):
        self.assertEqual(luigi_math.inc(a), a + 1)

    @given(integers(), integers())
    def test_multiply(self, a, b):
        self.assertEqual(luigi_math.multiply(a, b), a * b)

    @given(integers(), integers())
    def test_divide(self, a, b):
        assume(b != 0)
        self.assertEqual(luigi_math.divide(a, b), a / b)

    @given(integers(), integers())
    def test_power(self, a, b):
        assume(a < 100 and b < 100)
        assume(a > -100 and b > -100)
        assume(a != 0 and b != 0)
        self.assertEqual(luigi_math.power(a, b), math.pow(a, b))

    @given(integers())
    def test_power_2_inverts_sqrt(self, a):
        assume(a < 10000)
        assume(a > 0)
        self.assertEqual(luigi_math.power(a,2), luigi_math.sqrt(a ** 4))

if __name__ == '__main__':
    unittest.main()