
from reasonable import FloatStrategy


def test_basic_sanity():
    strat = FloatStrategy(0, 10, 8)

    expected = "<FloatStrategy 0 10 8>"
    assert str(strat) == expected

    assert 0 < strat.do_draw(None) < 10


if __name__ == '__main__':
    import pytest
    pytest.main()
