import pytest

from Lesson1.divi import division


@pytest.mark.parametrize("a,b,result", [(10, 2, 5),
                                        (20, 2, 10),
                                        (10, -2, -5)])
def test_div(a, b, result):
    assert division(a, b) == result


@pytest.mark.parametrize("excepted, first, second", [(ZeroDivisionError, 10, 0),
                                                     (TypeError, 10, "2")])
def test_div_zr(excepted, first, second):
    with pytest.raises(excepted):
        division(first, second)


def test_div_str():
    with pytest.raises(TypeError):
        division(10, "2")
