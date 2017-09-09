
import random

from hypothesis.searchstrategy.numbers import SearchStrategy


class FloatStrategy(SearchStrategy):
    def __init__(self, lower, upper, places):
        super().__init__()

        assert lower <= upper, "Invalid bounds"
        self._lower = lower
        self._upper = upper
        self._places = places

    def __repr__(self):
        name = self.__class__.__name__
        lower = self._lower
        upper = self._upper
        places = self._places
        return f"<{name} {lower} {upper} {places}>"

    def do_draw(self, data):
        num = random.uniform(self._lower, self._upper)
        return round(num, self._places)


class GaussianStrategy(SearchStrategy):
    """
    Gaussian (normally) distributed values
    with optional truncation and decimal places
    precision.
    """
    def __init__(self, mu, sigma, min_value, max_value, places):
        super().__init__()

        self._mu = mu
        self._sigma = sigma
        self._places = places
        self._min_value = min_value
        self._max_value = max_value

    def __repr__(self):
        name = self.__class__.__name__
        mu = self._mu
        sigma = self._sigma
        places = self._places
        return f"<{name} {mu} {sigma} {places}>"

    def do_draw(self, data):
        num = random.gauss(self._mu, self._sigma)
        if self._min_value:
            num = max(num, self._min_value)
        if self._max_value:
            num = min(num, self._max_value)
        return round(num, self._places)


if __name__ == '__main__':
    import pytest
    pytest.main()
