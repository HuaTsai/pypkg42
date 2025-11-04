import numpy as np
import pytest

from pypkg42.core.add import add, add_multiple


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 20) == 30

    def test_add_negative_numbers(self):
        assert add(-1, -2) == -3
        assert add(-5, -10) == -15

    def test_add_mixed_numbers(self):
        assert add(-1, 1) == 0
        assert add(5, -3) == 2
        assert add(-10, 15) == 5

    def test_add_zeros(self):
        assert add(0, 0) == 0
        assert add(5, 0) == 5
        assert add(0, 7) == 7

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestAddMultiple:
    def test_add_multiple_positive(self):
        assert add_multiple(1, 2, 3, 4) == 10
        assert add_multiple(10, 20, 30) == 60

    def test_add_multiple_single_number(self):
        assert add_multiple(5) == 5
        assert add_multiple(0) == 0

    def test_add_multiple_empty(self):
        assert add_multiple() == 0

    def test_add_multiple_mixed(self):
        assert add_multiple(1, -2, 3, -4) == -2
        assert add_multiple(10, -5, 3) == 8

    def test_add_multiple_numpy(self):
        arr = np.array([1, 2, 3])
        assert add_multiple(*arr) == 6
