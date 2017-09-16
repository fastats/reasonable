

from reasonable.strategies import GaussianStrategy


def gaussian(mu, sigma, min_value=None, max_value=None, places=8):
    """
    Returns normally distributed values from
    a Gaussian distribution with mean `mu` and
    standard deviation `sigma`.

    Values will be rounded to `places` decimal
    places (defaults to 8, the same as `pytest.approx`)

    .. code-block:: python

      gaussian(1.0, 0.4)
      gaussian(1.0, 0.4, min_value=0.5)

    .. note::
      `max_value` and `min_value` will cap and floor
      the data, they won't truncate it. This may
      result in data 'bunching' up against the
      constraints, and could meaningfully change the
      distribution.

    Usage:

    .. code-block:: python

      from reasonable import gaussian
      from hypothesis import given


      @given(gaussian(1.0, 0.4))
      def test_my_func(n):
          result = my_func(n)
    """
    return GaussianStrategy(mu, sigma, min_value, max_value, places)
