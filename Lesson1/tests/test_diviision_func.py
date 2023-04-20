import pytest

from Lesson1.divi import division


def test_div():
    assert division(10, 2) == 5.0
