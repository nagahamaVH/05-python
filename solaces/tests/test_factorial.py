import pytest
from solaces.lib.aula2 import factorial


class TestValidInput:
    def test_greater_than_one(self):
        import math

        assert factorial(4) == 24
        assert factorial(12) == math.factorial(12)

    def test_one(self):
        assert factorial(1) == 1

    def test_zero(self):
        assert factorial(0) == 1


class TestInvalidInput:
    def test_string(self):
        with pytest.raises(TypeError):
            factorial("2")

    def test_float(self):
        with pytest.raises(TypeError):
            factorial(32.4)

    def test_less_than_zero(self):
        with pytest.raises(ValueError):
            factorial(-3)

    def test_not_int(self):
        with pytest.raises(TypeError):
            factorial({3})
