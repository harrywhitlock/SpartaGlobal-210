
def fizzbuzz(x):

    if x % 3 == 0 and x % 5 == 0:
        return 'Fizzbuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'



def test_fizzbuzz():

    assert fizzbuzz(3) == 'Fizz'

    assert fizzbuzz(5) == 'Buzz'

    assert fizzbuzz(15) == 'Fizzbuzz'