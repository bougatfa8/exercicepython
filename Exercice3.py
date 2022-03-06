def Calc(x):
    return x * (x + 1) / 2

def triangular(number):
    num = 1
    for i in range(number):
        yield Calc(num)
        num = num + 1

number = int(input(" Please Enter any numeric Value : "))
x = triangular(number)
for i in range(number):
    tri = next(x)
    print(int(tri))
