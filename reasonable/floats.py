

from reasonable.strategies import FloatStrategy


def floats(vals, places=8):
    """

    """
    lower, upper = vals.get_bounds()
    return FloatStrategy(lower, upper, places)
