
from reasonable.strategies import GaussianStrategy


def test_basic_sanity():
    strat = GaussianStrategy(0, 1, None, None, 8)

    expected = "<GaussianStrategy 0 1 8>"
    assert str(strat) == expected

    assert -10 < strat.do_draw(None) < 10


def test_truncation():
    strat = GaussianStrategy(0, 1, 0.5, None, 8)
    assert 0.5 <= strat.do_draw(None) < 10


if __name__ == '__main__':
    import pytest
    pytest.main()
