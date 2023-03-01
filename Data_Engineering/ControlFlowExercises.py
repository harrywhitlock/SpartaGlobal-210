print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
print(x[:5])
# A1a:



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

for i in x:
    if i % 2 == 0:
        print(i)

# A1b:


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

for i in x[:5]:
    if i % 2 == 0:
        print(i)

# A1c:


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

first = []
for i in range(len(names)):
    first.append(names[i][0])

print(first)


# A2a:




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

space = []
for i in range(len(names)):
    space.append(names[i].index(' '))

print(space)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:


initials = []
full_initials = []

for i in range(len(names)):
    y = (names[i].split(" "))
    initials = [y[0][0], y[1][0]]
    full_initials.append(initials)

print(full_initials)




# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

for i in range(len(list_of_lists)):
    if len(list_of_lists[i]) == len(set(list_of_lists[i])):
        print(list_of_lists[i])


# A3a:


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
number = input('enter number greater than 100:')
while int(number) <= 100:
   number = input("enter new number")




print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

number = input('enter number:')

if int(number) > 100:
    for i in range(2, int(number)):
        if int(number) % i == 0:
            print('is not prime')
            break
        else:
            print('is prime')
            break

while int(number) <= 100:

    if int(number) == 0 or int(number) == 1:
        print('is not prime')
    elif int(number) == 2:
        print('is prime')

    for i in range(2, int(number)):
        if int(number) % i == 0:
            print('is not prime')
            break
        else:
            print('is prime')
            break
    number = input("enter new number")



