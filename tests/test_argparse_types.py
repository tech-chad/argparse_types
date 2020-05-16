"""
argparse_types function test file
"""
import pytest

import argparse_types


def _raises_test_case(func, *args):
    with pytest.raises(argparse_types.argparse.ArgumentTypeError):
        func(*args)


@pytest.mark.parametrize("test_values, expected_result", [
    ("1", 1),
    ("100", 100),
    ("20000000", 20000000)
])
def test_pos_int(test_values, expected_result):
    result = argparse_types.pos_int(test_values)
    assert result == expected_result


@pytest.mark.parametrize("test_values", [
    "0", "-1", "-500000", "letters", "1.1", "-1.1"
])
def test_pos_int_fails(test_values):
    _raises_test_case(argparse_types.pos_int, test_values)


@pytest.mark.parametrize("test_values, expected_result", [
    ("-1", -1),
    ("-100", -100),
    ("-2000000", -2000000)
])
def test_neg_int(test_values, expected_result):
    result = argparse_types.neg_int(test_values)
    assert result == expected_result


@pytest.mark.parametrize("test_values", [
    "0", "1", "500000", "letters", "1.1", "-1.1"
])
def test_neg_int_fails(test_values):
    _raises_test_case(argparse_types.neg_int, test_values)


def test_zero_int():
    result = argparse_types.zero_int("0")
    assert result == 0


def test_zero_int_multiple_zeroes():
    result = argparse_types.zero_int("0000")
    assert result == 0


@pytest.mark.parametrize("test_values", [
    "1", "50000", "letters", "-1", "-50000", "1.1", "-1.1"
])
def test_zero_int_fails(test_values):
    _raises_test_case(argparse_types.zero_int, test_values)
