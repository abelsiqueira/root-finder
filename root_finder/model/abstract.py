"""Defines the abstract model of a root-finding problem"""

from abc import ABC
from abc import abstractmethod
from ..exception import DerivativeNotDefined


class AbstractRootFindingProblem(ABC):
    """Abstract structure for a root-finding problem"""

    @abstractmethod
    def derivative_available(self):
        """Whether the derivative is available"""

    @abstractmethod
    def value(self, point):
        """The function value"""

    def derivative(self, point):
        """The derivative value"""
        raise DerivativeNotDefined

    @abstractmethod
    def reset(self):
        """Reset counter and possibly other attributes of the problem"""
