'''
1
22
333
4444
55555
'''
#1st method
for i in range(1,6):
    print(str(i)*i)

#2nd method
for i in range(1,6):
    for j in range(i):
        print(i, end=' ')
    print('\n',end='')