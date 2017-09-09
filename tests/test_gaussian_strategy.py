
import numpy as np
from scipy.stats import kstest

from reasonable.strategies import GaussianStrategy


def test_basic_sanity():
    strat = GaussianStrategy(0, 1, None, None, 8)

    expected = "<GaussianStrategy 0 1 8>"
    assert str(strat) == expected

    assert -10 < strat.do_draw(None) < 10


def test_truncation():
    strat = GaussianStrategy(0, 1, 0.5, None, 8)
    assert 0.5 <= strat.do_draw(None) < 10


def test_kolmogorov_smirnov_fit():
    """
    Kolmogorov-Smirnov tests the goodness of fit
    of the data to a given distribution.
    """
    strat = GaussianStrategy(0.0, 1.0, None, None, 8)
    data = [strat.do_draw(None) for x in range(10000)]
    arr = np.array(data, dtype='float32')

    t_stat, p_value = kstest(arr, 'norm')

    assert p_value < 0.95

if __name__ == '__main__':
    import pytest
    pytest.main()
