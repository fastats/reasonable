
from reasonable.floats import floats
from reasonable.strategies import FloatStrategy
from reasonable.x import x


MAJOR = 2017
MINOR = 1
POINT = '-pre-alpha'

version = [MAJOR, MINOR]
__version__ = '.'.join(map(str, version)) + POINT


__all__ = [
    floats,
    FloatStrategy,
    x,
    __version__
]
