"""Defines a manually inputted root-finding problem"""

from .. import exception
from .abstract import AbstractRootFindingProblem


class BasicRootFindingProblem(AbstractRootFindingProblem):
    """Model defined explicitly"""

    def __init__(self, start_point, func, grad=None):
        self.start_point = start_point
        self.func = func
        self.grad = grad
        self.neval_func = 0
        self.neval_deriv = 0

    def derivative_available(self):
        return self.grad is not None

    def value(self, point):
        self.neval_func += 1
        return self.func(point)

    def derivative(self, point):

        if self.grad is None:
            raise exception.DerivativeNotDefined

        self.neval_deriv += 1
        return self.grad(point)

    def reset(self):
        self.neval_func = 0
        self.neval_deriv = 0
