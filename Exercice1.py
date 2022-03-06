#Cubed Values from a Generator Object
def cube(num):
    return num * num * num
class Cubed:
    def __init__(self, nbrValue):
        self.nbrValue = nbrValue
        self.count = 1;
    def __iter__(self):
        return self
    def __next__(self):
        if self.count <= self.nbrValue:
            num = cube(self.count)
            self.count += 1
            return num
        else:
            raise StopIteration()
number = int(input(" Please Enter any numeric Value : "))
for i in Cubed(number):
    print(i)
