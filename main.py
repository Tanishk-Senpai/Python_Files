tup = ('tanishk','yash')
item = input("what search? ")
y = list(tup)
for i in range(len(tup)):
    if item.lower() == tup[i].lower():
        print('we have the item')
        print(y[i])
        del y[i]
    else:
        print('improve your memory')

x = tuple(y)
print(x)
