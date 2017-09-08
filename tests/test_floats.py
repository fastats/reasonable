
from hypothesis import given
from reasonable import floats, x


@given(floats((-5 < x) & (x < 5)))
def test_floats_basic_sanity(n):
    assert -5 < n < 5


@given(floats(x < 5))
def test_floats_less_than(n):
    assert n < 5


@given(floats(x > 1))
def test_floats_greater_than(n):
    assert n > 1


@given(floats(0 < x))
def test_floats_greater_than_reverse(n):
    assert n > 0


@given(floats((-0.001 < x) & (x < 0.001)))
def test_small_range(n):
    assert -0.001 < x < 0.001


if __name__ == '__main__':
    import pytest
    pytest.main()
