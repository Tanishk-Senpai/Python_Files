'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''
#1st method
column = 5
num = 0
for i in range(column,0,-1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    num = 0
    print('\n',end ='')

'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
'''
columns = 6
for i in range(columns,0,-1):
    for j in range(0,i):
        print(j,end=" ")
    print('')
