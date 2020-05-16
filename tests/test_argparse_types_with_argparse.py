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
def test_neg_int_full_fail(test_values, capsys):
    _argparse_runner_raises(argparse_types.zero_int, test_values)
    captured = capsys.readouterr().err
    assert f"{test_values} is an invalid zero int value" in captured
