
from hypothesis import given
from reasonable import gaussian


@given(gaussian(1.0, 0.4, places=6))
def test_basic_sanity(n):
    assert -10 < n < 10


@given(gaussian(1.0, 0.4, min_value=0.5))
def test_min_value_truncation(n):
    assert 0.5 <= n


@given(gaussian(2.0, 1.0, max_value=1.5))
def test_max_value_truncation(n):
    assert n <= 1.5


if __name__ == '__main__':
    import pytest
    pytest.main()
