
import operator as op
import sys

__all__ = ['x']


class Numeric:
    def __gt__(self, other):
        return Term(self, op.gt, other)

    def __lt__(self, other):
        return Term(self, op.lt, other)

    def __ge__(self, other):
        return Term(self, op.ge, other)

    def __le__(self, other):
        return Term(self, op.le, other)

    def __and__(self, other):
        return Term(self, op.and_, other)


class Term(Numeric):
    def __init__(self, left, op, right):
        self._left = left
        self._op = op
        self._right = right

    def get_bounds(self):
        lower, upper = -sys.maxsize, sys.maxsize

        if isinstance(self._left, Term):
            lower, upper = self._left.get_bounds()
        if isinstance(self._right, Term):
            lower, upper = self._right.get_bounds()

        if isinstance(self._left, Numeric):
            if self._op in (op.gt, op.ge):
                lower = self._right
            else:
                upper = self._right

        if isinstance(self._right, Numeric):
            if self._op in (op.gt, op.ge):
                upper = self._left
            else:
                lower = self._left

        if isinstance(lower, Term):
            lower, _ = lower.get_bounds()
        if isinstance(upper, Term):
            _, upper = upper.get_bounds()

        return lower, upper


x = Numeric()
