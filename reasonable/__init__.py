
from reasonable.floats import floats
from reasonable.gaussian import gaussian
from reasonable.strategies import (
  FloatStrategy, GaussianStrategy
)
from reasonable.x import x


MAJOR = 2017
MINOR = 1
POINT = '-pre-alpha'

version = [MAJOR, MINOR]
__version__ = '.'.join(map(str, version)) + POINT


__all__ = [
    floats,
    FloatStrategy,
    gaussian,
    GaussianStrategy,
    x,
    __version__
]
