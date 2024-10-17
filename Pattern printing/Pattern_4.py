'''
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
'''

column = 5
num = 5

for i in range(column,0,-1):
    for j in range(1,i+1):
        print(num,end=" ")
    print('\n',end = '')