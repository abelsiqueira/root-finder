"""Exceptions"""

class RootFindingError(ValueError):
    """All exceptions related to root-finder"""

class DerivativeNotDefined(RootFindingError):
    """Derivate is not available but was called"""
