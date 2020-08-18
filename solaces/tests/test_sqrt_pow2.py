import pytest
from solaces.lib.aula2 import _sqrt_pow2


def test_power2():
    x = -5
    y = -1.2
    assert _sqrt_pow2(x) == x ** 2
    assert _sqrt_pow2(y) == y ** 2


def test_sqrt():
    import math
    x = 12
    y = 0
    z = 81
    assert _sqrt_pow2(x) == math.sqrt(x)
    assert _sqrt_pow2(y) == math.sqrt(y)
    assert _sqrt_pow2(z) == math.sqrt(z)


class TestInvalidInput:
    def test_string(self):
        with pytest.raises(TypeError):
            _sqrt_pow2("156")

    def test_non_numeric_object(self):
        with pytest.raises(TypeError):
            _sqrt_pow2([512])
