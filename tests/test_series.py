import pytest
# from package_name.module_name import function_name
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_exists():
    assert fibonacci

def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_lucas_exists():
    assert lucas

def test_lucas_15():
    actual = lucas(15)
    expected = 1364
    assert actual == expected

def test_sum_fib():
    actual = sum_series(8)
    expected = 21
    assert actual == expected

def test_sum_lucas():
    actual = sum_series(8, 2, 1)
    expected = 47
    assert actual == expected