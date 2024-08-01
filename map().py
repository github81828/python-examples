#The map() function iterates through all items in the given iterable and executes 
# the function we passed as an argument on each of them.
#The syntax is:
#map(function, iterable(s))

#to add 10 for each element
list1=[1,2,3,4,5,6]
def element (n):
    return n+10
list(map(element,list1))

#to find square of each no.
list1=[1,2,3,4,5,6]
def element (n):
    return n*n
list(map(element,list1))


#REDUCE()
# reduce() works differently than map() and filter(). It does not return a new list based on the function 
# and iterable we've passed. Instead, it returns a single value. 
# The syntax is:
#reduce(function, sequence[, initial]   
list1=[1,2,3,4,5,6]
sum=0
for element in list1:
  sum=sum+element
print(sum)


def shafna(a):
  sum=0
  sum=sum+element
  return sum

def shafna1(a,b):
   return a+b
   
import functools
print(functools.reduce(shafna1,list1)) 
print(functools.reduce(lambda a,b:a+b,list1))



