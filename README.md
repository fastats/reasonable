# reasonable

[![Build Status](https://travis-ci.org/fastats/reasonable.svg?branch=master)](https://travis-ci.org/fastats/reasonable)
[![codecov](https://codecov.io/gh/fastats/reasonable/branch/master/graph/badge.svg)](https://codecov.io/gh/fastats/reasonable)


Reasonable float handling for Hypothesis testing
---

[Hypothesis](https://hypothesis.works) is an excellent package, however sometimes we want to trade the purist approach towards floating-point numbers for a more pragmatic approach.

`reasonable` complements `hypothesis` by limiting the range and precision of generated floats, defaulting to 8d.p. 

As a result, `reasonable` does not generate very small (10^-300) floats, which makes approximate comparisons (of the sort used in unit-tests) much easier to perform.

For example, by replacing `floats` with the version in `reasonable`, you can perform approximate comparisons:

```
from hypothesis import given
from pytest import approx
from reasonable import floats, x

@given(floats(x < 0.0))
def test_minimizer(n):
    result = minimize(my_func, x0=n)
    assert result == approx(0.23456789)
```

#### Installation

Requirements: You will need hypothesis installed (obviously) - 

```
pip install hypothesis
```

then install `reasonable` with

```
pip install reasonable
```

#### Contributing

All contributions are welcome :)

If you would like to contribute anything, open a PR (issues are turned off):

- To report a bug, open a PR with a unit-test that fails.
- To request an API change/new functionality, open a PR with a unit-test that fails showing your preferred API.
- To submit a fix, open a PR with passing unit-tests and doctests. 

Doctests should be minimal and serve as API docs for the most common use cases. 

Unit-tests should be exhaustive, and include `basic sanity` tests as well as generative tests using `hypothesis`.
