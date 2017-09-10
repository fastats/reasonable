

from reasonable.strategies import FloatStrategy


def floats(vals, places=8):
    """
    `floats` is a replacement for the `hypothesis` `floats` 
    function.

    It requires at least one positional argument, using the 
    built-in `x` object available in `reasonable`.

    To use this `floats` function, set your constraints for 
    min/max values using the `x`-object

    .. code-block:: python
    
      floats(x > 1.0)
      floats(x <= 2.4)
      floats((50.0 < x) & (x < 70.0))

    .. note::
      In order to use multiple constraints, you must use the 
      bit-wise operator `&` **not** the boolean statement `and`. 
      This is a limitation of python in that `and` cannot be 
      overloaded, but `&` can.
    """
    lower, upper = vals.get_bounds()
    return FloatStrategy(lower, upper, places)
