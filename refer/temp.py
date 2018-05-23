import unittest
from parameterized import parameterized, param

# A list of tuples
@parameterized([
    (2, 3, 5),
    (3, 5, 8),
])
def test_add(a, b, expected):
    # assert_equal(a + b, expected)
    print(a,b,expected)
# A list of params
@parameterized([
    param("10", 10),
    param("10", 16, base=16),
])
def test_int(str_val, expected, base=10):
    pass

if __name__ == '__main__':
    unittest.main()