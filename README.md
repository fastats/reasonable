# reasonable

[![Build Status](https://travis-ci.org/fastats/reasonable.svg?branch=master)](https://travis-ci.org/fastats/reasonable)
[![codecov](https://codecov.io/gh/fastats/reasonable/branch/master/graph/badge.svg)](https://codecov.io/gh/fastats/reasonable)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9a41254b85564566913047e65e5f9518)](https://www.codacy.com/app/dave.willmer/reasonable?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fastats/reasonable&amp;utm_campaign=Badge_Grade)
[![Documentation Status](https://readthedocs.org/projects/reasonable/badge/?version=latest)](http://reasonable.readthedocs.io/en/latest/?badge=latest)


Reasonable float handling for Hypothesis testing
---

[Hypothesis](https://hypothesis.works) is an excellent package, however sometimes we want to trade the purist approach towards floating-point numbers for a more pragmatic approach.

`reasonable` complements `hypothesis` by limiting the range and precision of generated floats, defaulting to 8d.p. 

As a result, `reasonable` does not generate very small (10^-300) floats, which makes approximate comparisons (of the sort used in unit-tests) much easier to perform.

For example, by replacing `floats` with the version in `reasonable`, you can perform approximate comparisons:

```python
from hypothesis import given
from pytest import approx
from reasonable import floats, x

@given(floats(x < 0.0))
def test_minimizer(n):
    result = minimize(my_func, x0=n)
    assert result == approx(0.23456789)
```

#### Documentation

[reasonable.readthedocs.io](http://reasonable.readthedocs.io/en/latest/)

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

#### How to report a bug

- Create a new python file in the `tests` folder, make sure the filename starts with `test_`.
- Create a single function in the file which replicates the bug. Make sure the function name starts with `test_`.
- Open a PR with the new file and a brief description - the unit-tests should fail.

At that point either the reporter or a fastats developer can commit on that PR to fix the bug.
