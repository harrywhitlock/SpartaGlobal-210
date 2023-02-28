def isprime2(x):


    try:
        for i in range(2, x):
            if x % i == 0:
                return False
                break
            else:
                return True
    except TypeError:
        print('not a number')
        return False

print(isprime2(5))