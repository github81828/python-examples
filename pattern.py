#pattern 
#simple half pyramid pattern


#to print 10stars
print('*'*10)


for i in range(4):
    print('*'*6)


#? 
'''
*
**
***
****
*****
****** '''
for i in range(6):
    print("*"*(i+1))

    #herei=0  so it will print 1*
    #  for 2* we3 add (i+1) 
    # 6 means it will print 6*


#?
'''
*
**
***
****
*****
******
*******
********
*********
**********'''
for i in range(10):
      print("*"*(i+1))


#?
''''
*
* *
* * *
* * * *
* * * * *'''
a = 5
for i in range(1, a+1):
    print("* " * i)


#?
for i in range(5):
        print('* '*(i+1))


 # Left triangle star pattern
'''
    *
   **
  ***
 ****
*****
'''
 
a = 5
for i in range(1, a+1):
    print(" " * (a - i) + "*" * i)


#?
a=10
for i in range(0,a+1):
    print(' '*(a-i)+"*"*i)


rows = 5
for j in range(1, rows+1):
    print("*  " * j)

#?
a=5
for i in range(1,a+1):
    print(' '*(a-i)+"*"*i)

a=5
for i in range(a+1):
    print("*"*(a-i)+" "*i)



for i in range(5):
    print("*"*(i+1))


for i in range(5,0,-1):
    print('*'*i)


a=5
for i in range(5,1,-1):
    print(' '*i+'*'*(a-i))
    


# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")

rows=5
for i in range(0,rows):
    for j in range(0,i+1):
        print('*',end='')
    print("\r")


rows=5
for i in range(0,rows):


    for j in range(0,i+1):
        print('*',end='')

#RIGHT TRIANGLE PYRAMID OF STARS


rows = 5 # number of rows
k=2* rows - 2
for i in range(0, rows):
 for j in range(0, k):  # process each column
      print(end=" ")  # print space in pyramid
k = k - 2
for j in range(0, i + 1):
 print("* ", end="")  # display star
print("")


rows = 5
for j in range(1, rows+1):
    print("* " * j)

# Left triangle star pattern
size = 5
for i in range(1, size+1):
    print(" " * (size - i) + "*" * i)


    # downward triangle star pattern
n = 5

for i in range(n):

    # internal loop run for n - i times
    for j in range(n - i):
        print('*', end='')
    print()

#?
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

for i in range(1,6):
    print(" "*(n-i),"*"*i)

for i in range (1,6):
    for j in range(6-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()


n=5
for i in range (1,n+1):
    for j in range(n-i):
        print('',end='') 
    for j in range (2*i-1):
        print('*',end='')
    print()

rows = 5
space = 2 * rows - 2
for i in range(rows, -1, -1):

    for j in range(space, 0, -1):
        print(end=" ")
    space += 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")


n=5
for i in range(1,n+1):
    print(' '*n, end='') # repet space for n times
    print('* '*(i)) # repeat stars for i times
    n-=1

# to display stars in equilateral triangular form 
n=20
for i in range(1, 11):
    print(' '*(n-i) + '* '*(i))
''' 

  *  *  *  *  *
   *  *  *  *
    *  *  *
     *  *
       *

      '''
n=6
for i in range(1, n+1):
    print( ' '*(i)+' * '*(n-i))

n=5
for i in range(1,n+1,2):
  print(' '*(n-i)+' * ' *(i))
    
n=5
for i in range(1,n+1):
  print(' '*(n-i)+' *' *(i))


''''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
#
rows = 5
for i in range(1, rows + 1):#for raws
    for j in range(1, i + 1):#for columns
        print(j, end=' ')#j for clmns   ' 'for space
    print('')#for next line
#
rows = 5
for i in range(1, rows + 1):#for raws
    for i in range(1, i + 1):#for columns
        print(i, end=' ')
    print('')

 # 
''''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
rows = 5   
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

    row=5
    for i in range(row, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
#
''''
      1 
     1 2 
   1 2 3 4 
 1 2 3 4 5 6 
1 2 3 4 5 6 7 8
'''


rows = 6
for i in range(0,rows-1,1):
        for j in range(rows-i):
            print(" ",end='')
        for j in range(i + 1):
            print(j+1, end=' ')
        print()

'''''''''
   1   2   3   4   5   6
    1   2   3   4   5
      1   2   3   4
        1   2   3
          1   2
            1
'''''''''

n=6
for i in range (n-1,-1,-1):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print(' ',j+1,end=' ')
    print()




n=10
for i in range(1,n+1):
    print(''*(n-1),end=' ')
for j in range(1,i+1):
      print(j,end='')
print()
for i in range(n-1,0,-1):
     print(" "*(n-1),end=' ')
for j in range(1,i+1):
       print(j,end='')
print()


# diamond number pattern
n = 5
#upward
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print(j+1, end='')
    print()
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        print(j+1, end='')
    print()


for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print(j+1, end='')
    print()

n=10
for i in range(0,n+1):
    for j in range(0,n-i-1):
        print(end=' ')
    for j in range(0,i+1):
        print('*',end='')
    print()
        