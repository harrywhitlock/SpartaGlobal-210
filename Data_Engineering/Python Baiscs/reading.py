filename = "sample.txt"
file = open(filename, mode='r')
text = file.read()
print(text)

try:
    with open(filename) as file:
        print(file.read())

except:
    print('the file counld not be read')