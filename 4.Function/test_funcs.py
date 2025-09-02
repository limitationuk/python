from funcs import even, avg, max, min

def test_even():
    assert True == even(10)
    assert False == even(7)

value = [10, 20, 30]

def test_avg():
    assert 20 == avg(value)

def test_max():
    assert 30 == max(value)

def test_min():
    assert 10 == min(value)