import calculations

def test_add1():
    assert calculations.add(1,2)==3;
    assert calculations.add(3,4)==7;

def test_add2():
    assert calculations.add('Hello', 'Du')=='HelloDu';
    assert calculations.add(10,10)==20;