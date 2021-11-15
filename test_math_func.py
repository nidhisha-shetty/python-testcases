import math_func

def test_add():
    assert math_func.add(5,7)==12
    assert math_func.add(6.2,3.8)==10.0
    assert math_func.add(3,4)==7
    assert math_func.add(8,7)==15

def test_sub():
    assert math_func.sub(3,2)==1
    assert math_func.sub(9,6)==3
    assert math_func.sub(10.0,6.2)==3.8
    assert math_func.sub(9.2,6.0)==3.2
