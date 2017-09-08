
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
        return (f"<{self.__class__.__name__} "
                "{self._lower_bound} "
                "{self._upper_bound}"
                "{self._places}")

    def do_draw(self, data):
        num = random.uniform(self._lower, self._upper)
        return round(num, self._places)


if __name__ == '__main__':
    import pytest
    pytest.main()
