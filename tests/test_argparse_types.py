"""
argparse_types function test file
"""
import pytest

import argparse_types


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
    with pytest.raises(argparse_types.argparse.ArgumentTypeError):
        argparse_types.pos_int(test_values)


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
    with pytest.raises(argparse_types.argparse.ArgumentTypeError):
        argparse_types.neg_int(test_values)
