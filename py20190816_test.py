from py20190816 import less_number

def test_less_number():
    assert less_number(10,20) == 10
    assert less_number(20,10) == 10
    assert less_number(30,10) == 10