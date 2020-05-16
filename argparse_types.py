import argparse


def pos_int(value: str) -> int:
    """ Positive int value not including 0"""
    error_msg = f"{value} is not a positive int"
    try:
        int_value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(error_msg)
    else:
        if int_value <= 0:
            raise argparse.ArgumentTypeError(error_msg)
        else:
            return int_value


def neg_int(value: str) -> int:
    error_msg = f"{value} is an invalid negative int value"
    try:
        int_value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(error_msg)
    else:
        if int_value >= 0:
            raise argparse.ArgumentTypeError(error_msg)
        else:
            return int_value


def zero_int(value: str) -> int:
    """ Zero int value. """
    # will allow a string with multiple zeroes to work and return
    # in single int 0.  Not sure if this should be.
    error_msg = f"{value} is an invalid zero int value"
    try:
        int_value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(error_msg)
    else:
        if int_value != 0:
            raise argparse.ArgumentTypeError(error_msg)
        else:
            return int_value
