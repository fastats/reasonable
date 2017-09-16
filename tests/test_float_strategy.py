
import numpy as np
from pytest import approx
from scipy.stats import kstest

from reasonable import FloatStrategy


def test_basic_sanity():
    strat = FloatStrategy(0, 10, 8)

    expected = "<FloatStrategy 0 10 8>"
    assert str(strat) == expected

    assert 0 < strat.do_draw(None) < 10


def test_kolmogorov_smirnov_fails():
    """
    Confirms that the Kolmogorov-Smirnov
    test for goodness-of-fit allows us to
    reject the hypothesis of a normal
    distribution.
    """
    strat = FloatStrategy(0, 10, 8)
    data = [strat.do_draw(None) for x in range(10000)]
    arr = np.array(data, dtype='float32')

    _, p_value = kstest(arr, 'norm')

    assert p_value == approx(0.0)



if __name__ == '__main__':
    import pytest
    pytest.main()
