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


@pytest.mark.parametrize("test_values, expected_results", [
    ("1.1", 1.1),
    ("200.23", 200.23),
    ("45000.650", 45000.650)
])
def test_pos_float(test_values, expected_results):
    result = argparse_types.pos_float(test_values)
    assert result == expected_results


@pytest.mark.parametrize("test_values", [
    "0", "0.0", "-25.50", "-5", "5", "string", "52500"
])
def test_pos_float_fails(test_values):
    _raises_test_case(argparse_types.pos_float, test_values)


@pytest.mark.parametrize("test_values, expected_results", [
    ("-1.1", 1.1),
    ("-350.0", -350.0),
    ("-80250.250", -80250.250)
])
def test_neg_float(test_values, expected_results):
    result = argparse_types.neg_float(test_values)
    assert result == expected_results


@pytest.mark.parametrize("test_values", [
    "0", "0.0", "25.25", "500", "-500", "string"
])
def test_neg_float(test_values):
    _raises_test_case(argparse_types.neg_float, test_values)


def test_zero_float():
    result = argparse_types.zero_float("0.0")
    assert result == 0.0


@pytest.mark.parametrize("test_values, expected_results", [
    ("0.000", 0.0),
    ("00.0", 0.0),
    ("00.00", 0.0),
])
def test_zero_float_multiple_zeroes(test_values, expected_results):
    result = argparse_types.zero_float(test_values)
    assert result == expected_results


@pytest.mark.parametrize("test_values", [
    "-5", "-5.5", "5", "-500", "string",
])
def test_zero_float_fail(test_values):
    _raises_test_case(argparse_types.zero_float, test_values)


@pytest.mark.parametrize("test_value, expected_result", [
    ("1", 1), ("400", 400), ("0", 0), ("-400", -400),
    ("1.5", 1.5), ("4564.99343", 4564.99343), ("-45.390", -45.390),
])
def test_int_float(test_value, expected_result):
    result = argparse_types.int_float(test_value)
    assert result == expected_result


@pytest.mark.parametrize("test_value", [
    "test45", "alpha", "5*6", "rt.78", "56 56", "99-34",
])
def test_int_float_fail(test_value):
    _raises_test_case(argparse_types.int_float, test_value)


@pytest.mark.parametrize("test_values, expected_results", [
    ("True", True),
    ("False", False),
    ("None", None),
])
def test_bool_none(test_values, expected_results):
    result = argparse_types.bool_none(test_values)
    assert result == expected_results


@pytest.mark.parametrize("test_values", [
    "0", " ", "string", "1234", "25.25", "-34", "-34.34",
    "true", "false", "none", "NONE", "TRUE", "FALSE", "NULL",
])
def test_bool_none_fail(test_values):
    _raises_test_case(argparse_types.bool_none, test_values)


@pytest.mark.parametrize("test_values", [
    "192.168.0.1", "0.0.0.0", "127.0.0.0", "255.255.255.255"
])
def test_ip4(test_values):
    result = argparse_types.ip4(test_values)
    assert result == test_values


@pytest.mark.parametrize("test_values", [
    "19216801", "300.300.300.300", "string", "-500", "192.168.2.98:120",
    "0.0.0", "192.300.5.1", "1.2.3", "192.168.3.55.120", "192.sdf.30.5",
    "192.168.1.256", "192.168.1.1-100", "192.168..1", "192,168,2,100",
])
def test_ip4_fail(test_values):
    _raises_test_case(argparse_types.ip4, test_values)
