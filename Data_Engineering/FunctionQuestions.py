print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def function(x):

    divisor = []
    for i in range(1, x+1):
        if x % i == 0:
            divisor.append(i)
    return divisor

print(function(12))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def function2(x, y):
    if x % y == 0 or y % x == 0:
        return True
    else: return False

print(function2(2, 3))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def function3(x):
    return alphabet.index(x) + 1

print(function3('b'))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def function4(x):
    id = []
    for i in x:
        id.append(alphabet.index(i))
    mystring = ""

    for digit in id:
        mystring += str(digit)
    return mystring

print(function4('bob'))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def function5(x):
    id = []
    for i in x:
        id.append(alphabet.index(i))




    mystring = ""
    for digit in id:
        mystring += str(digit)
    newlist = []
    for digit in mystring:
        newlist.append(int(digit))

    total = 0
    for i in newlist:
        total += i

    print(newlist)

    return int(mystring) - int(total)

print(function5('bob'))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def isprime(x):

    if int(x) == 0 or int(x) == 1:
        return False
    if int(x) == 2:
        return True


    for i in range(2, int(x) - 1):
        if int(x) % i == 0:
            return False
            break
        else:
            return True
            break

print(isprime(2))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def isprime2(x):

#    new_string = str(x).replace('.', '')
#   new_string = new_string.replace('-', '')
#   if new_string.isnumeric() != True:
#       return 'Not a number'

    if isinstance(x, int) != True:
        return ('Not an integer')
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True


    try:
        for i in range(2, int(x)):
            if int(x) % i == 0:
                return False
                break
            else:
                return True
    except TypeError:
        print('not a number')
        return False

print(isprime2(1))


# -------------------------------------------------------------------------------------- #






