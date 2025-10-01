from unilab import hello, mean
import pytest

def test_hello():
    assert "Hello" in hello("Nilton")

def test_mean():
    assert mean([1, 2, 3]) == 2
    with pytest.raises(ValueError):
        mean([])