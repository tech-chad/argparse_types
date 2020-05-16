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
