import pytest
from solaces.lib.aula2 import _sqrt_pow2


def test_power2():
    x = -1.2
    assert _sqrt_pow2(x) == x ** 2


def test_sqrt_greater_than_zero():
    import math
    x = 12.3
    assert _sqrt_pow2(x) == math.sqrt(x)


def test_sqrt_zero():
    assert _sqrt_pow2(0) == 0


class TestInvalidInput:
    def test_string(self):
        with pytest.raises(TypeError):
            _sqrt_pow2("156")

    def test_non_numeric_object(self):
        with pytest.raises(TypeError):
            _sqrt_pow2([512])
