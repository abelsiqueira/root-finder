"""Test models"""
from dataclasses import dataclass
from math import exp
import pytest

from root_finder.model.abstract import AbstractRootFindingProblem
from root_finder.model.basic import BasicRootFindingProblem
from root_finder.exception import DerivativeNotDefined

def test_abstract_model():
    """All tests related to the abstract root-finding model"""
    AbstractRootFindingProblem.__abstractmethods__ = set()
    @dataclass
    class DummyRFP(AbstractRootFindingProblem):
        """dummy"""

    rfp = DummyRFP()
    assert rfp.derivative_available() is None
    assert rfp.value(0.0) is None
    assert rfp.reset() is None
    with pytest.raises(DerivativeNotDefined):
        rfp.derivative(0.0)

def test_basic_model_only_value():
    """Test the basic model when the derivative is not available"""
    value = lambda x: x * exp(-x) - 1
    rfp = BasicRootFindingProblem(1.0, value)
    assert rfp.start_point == 1.0
    assert rfp.neval_func == 0
    assert rfp.neval_deriv == 0
    assert rfp.derivative_available() is False
    for point in [-1.5, 0.5, 3.14]:
        assert value(point) == rfp.value(point)
        with pytest.raises(DerivativeNotDefined):
            rfp.derivative(point)
    assert rfp.neval_func == 3
    assert rfp.neval_deriv == 0
    rfp.reset()
    assert rfp.neval_func == 0

def test_basic_model_value_and_deriv():
    """Test the basic model when the derivative is available"""
    value = lambda x: x * exp(-x) - 1
    deriv = lambda x: exp(-x) * (1 - x)
    rfp = BasicRootFindingProblem(1.0, value, deriv)
    assert rfp.start_point == 1.0
    assert rfp.neval_func == 0
    assert rfp.neval_deriv == 0
    assert rfp.derivative_available() is True
    for point in [-1.5, 0.5, 3.14]:
        assert value(point) == rfp.value(point)
        assert deriv(point) == rfp.derivative(point)
    assert rfp.neval_func == 3
    assert rfp.neval_deriv == 3
    rfp.reset()
    assert rfp.neval_func == 0
    assert rfp.neval_deriv == 0
