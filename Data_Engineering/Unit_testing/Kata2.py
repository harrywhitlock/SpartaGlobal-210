
from addition import Add



def test_1():

    assert Add("") == 0

def test_2():
    assert Add('1') == 1

def test_3():
    assert Add('1,2') == 3


    #unknown number of argument
def test_4():
    assert Add('1,2\n3') == 6

def test_5():
    assert Add('1,2,') == 'Error'
