

from reasonable.strategies import GaussianStrategy


def gaussian(mu, sigma, min_value=None, max_value=None, places=8):
    """
    Returns normally distributed values from
    a Gaussian distribution with mean `mu` and
    standard deviation `sigma`.

    Values will be rounded to `places` decimal
    places.
    """
    return GaussianStrategy(mu, sigma, min_value, max_value, places)
