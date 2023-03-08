
class fizzbuzz():

    def __init__(self, n):
        self.n = n
        #for i in range(self.n):
            #print(i)

    def fizz(self):

        for i in range(self.n):
            if i % 3 == 0:
                print(str(i) + ' fizz')

    def buzz(self):
        for i in range(self.n):
            if i % 5 == 0:
                print(str(i) + ' buzz')

    def fizzbuzz(self):
        for i in range(self.n):
            if i % 3 == 0 and i % 5 == 0:
                print(str(i) + ' fizzbuzz')

f = fizzbuzz(100)
f.fizz()
f.buzz()
f.fizzbuzz()
