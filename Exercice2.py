def negative(nbrValues):

    for i in range(1,nbrValues * 2 ,2):
        yield -i

number = int(input(" Please Enter any numeric Value : "))

for i in negative(number):
    print(i)
