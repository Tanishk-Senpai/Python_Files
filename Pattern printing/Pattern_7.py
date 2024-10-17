'''
* * * *
 * * *
  * *
   *
'''

star_column = 4
blank_column = 0
for i in range(star_column,0,-1):
    for k in range(blank_column,0,-1):
        print(' ',end = '')
    blank_column += 1
    for j in range(star_column):
        print('*', end=' ')
    star_column = star_column - 1
    print('')