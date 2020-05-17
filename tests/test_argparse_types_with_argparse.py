import argparse
import pytest

import argparse_types


def _argparse_runner(test_type, test_values):
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", dest="test_type", type=test_type)
    args = parser.parse_args(["-t", str(test_values)])
    return args.test_type


def _argparse_runner_raises(test_type, test_values):
    with pytest.raises(SystemExit):
        _argparse_runner(test_type, test_values)


@pytest.mark.parametrize("test_values, expected_results", [
    ("10", 10),
    ("5000000", 5000000),
])
def test_pos_int_full(test_values, expected_results):
    result = _argparse_runner(argparse_types.pos_int, test_values)
    assert result == expected_results


@pytest.mark.parametrize("test_values", [
    "0", "-100", "string", "1.1", ":*&"
])
def test_pos_int_full_fail(test_values, capsys):
    _argparse_runner_raises(argparse_types.pos_int, test_values)
    captured = capsys.readouterr().err
    assert f"{test_values} is not a positive int" in captured


@pytest.mark.parametrize("test_values, expected_results", [
    ("-10", -10),
    ("-5000000", -5000000),
])
def test_neg_int_full(test_values, expected_results):
    result = _argparse_runner(argparse_types.neg_int, test_values)
    assert result == expected_results


@pytest.mark.parametrize("test_values", [
    "0", "100", "string", "1.1", ":*&"
])
def test_neg_int_full_fail(test_values, capsys):
    _argparse_runner_raises(argparse_types.neg_int, test_values)
    captured = capsys.readouterr().err
    assert f"{test_values} is an invalid negative int value" in captured


@pytest.mark.parametrize("test_values, expected_results", [
    ("0", 0),
    ("000000", 0),
])
def test_zero_int_full(test_values, expected_results):
    result = _argparse_runner(argparse_types.zero_int, test_values)
    assert result == expected_results


@pytest.mark.parametrize("test_values", [
    "-34", "100", "string", "1.1", ":*&"
])
def test_zero_int_full_fail(test_values, capsys):
    _argparse_runner_raises(argparse_types.zero_int, test_values)
    captured = capsys.readouterr().err
    assert f"{test_values} is an invalid zero int value" in captured


@pytest.mark.parametrize("test_values, expect_results", [
    ("25.0", 25.0),
    ("352.25", 352.25),
])
def test_pos_float_full(test_values, expect_results):
    result = _argparse_runner(argparse_types.pos_float, test_values)
    assert result == expect_results


@pytest.mark.parametrize("test_values", [
    "0", "-2.25", "string", "300",
])
def test_pos_float_full_fail(test_values, capsys):
    _argparse_runner_raises(argparse_types.pos_float, test_values)
    captured = capsys.readouterr().err
    assert f"{test_values} is an invalid positive float" in captured


@pytest.mark.parametrize("test_values, expected_results", [
    ("-25.25", -25.25),
    ("-500.0", -500.0),
])
def test_neg_float_full(test_values, expected_results):
    result = _argparse_runner(argparse_types.neg_float, test_values)
    assert result == expected_results


@pytest.mark.parametrize("test_values", [
    "0", "2.25", "-25", "string"
])
def test_neg_float_full_fail(test_values, capsys):
    _argparse_runner_raises(argparse_types.neg_float, test_values)
    captured = capsys.readouterr().err
    assert f"{test_values} is an invalid negative float" in captured


def test_zero_float_full():
    result = _argparse_runner(argparse_types.zero_float, "0.0")
    assert result == 0.0


@pytest.mark.parametrize("test_values", [
    "1.1", "-200.0", "200", "500.50", "string",
])
def test_zero_float_full_fails(test_values, capsys):
    _argparse_runner_raises(argparse_types.zero_float, test_values)
    captured = capsys.readouterr().err
    assert f"{test_values} is an invalid zero float" in captured


@pytest.mark.parametrize("test_values", [
    "0.0.0.0", "127.0.0.0", "192.168.1.50", "255.255.255.255",
])
def test_ip4_full(test_values):
    result = _argparse_runner(argparse_types.ip4, test_values)
    assert result == test_values


@pytest.mark.parametrize("test_values", [
    "-255", "1.2.3", "192.168.1.356", "192.168.0.50:130", "string",
    "192.168.1.1.1",
])
def test_ip4_full_fail(test_values, capsys):
    _argparse_runner_raises(argparse_types.ip4, test_values)
    captured = capsys.readouterr().err
    assert f"{test_values} is an invalid ip4 address" in captured
