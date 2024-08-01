#FUNCTION

#to print sum of the list
list1=[1000,2000]
sum=0
for variable in list1:
    sum=sum+variable
print(sum)


list1=[1000,2000]
sum=0
for variable in list1:
    sum=sum+variable
print(sum)
def shafna(a):
    sum=0
    for variable in list1:
        sum=sum+variable
    return sum
    
shafna(list1)



#to find even numbers in list1
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
def even(a):
 for value in list1:
    if value%2==0:
        list2.append(value)
 return list2

even(list2)


#to find odd values
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
list3=[]
def even (a):
 for value in list1:
    if value%2==0:
        list2.append(value)
    else:
       list3.append(value)
 return list2,list3

a=even(list2)
a[1]


#write a python function that accepts a string and counts the no. of upper and lower case letters
i=input('enter the value')
def value (i):#value=function   i=parameter
   lower=0
   upper=0
   for value in i:
      if value.islower():
        lower=lower+1
      else:
        upper=upper+1
   return upper,lower
         
print(value(i))

#by adding no.
i=input('enter the value')
def value (i):#value=function   i=parameter
   lower=0
   upper=0
   number=0
   for value in i:
      if value.islower():
        lower=lower+1
      elif value.isupper():
        upper=upper+1  
      else:
       number=number+1
   return upper,lower,number        
print(value(i))
#write a python function to check weather a no.falls within a given range
r=int(input('enter the number'))
def range1(r):
   if r in range(100):
      print(True)
   else:
      print(False)
range1(r)


         



