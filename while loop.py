i=int(input("enter a value"))
sum=0
while i!=0:
    sum=sum+i
    i=int(input("enter a value"))
    print(sum)
print(sum)

#to print sum <500
i=int(input("enter a value"))
sum=0
while sum<500:
    sum=sum+i
    i=int(input("enter a value"))
    
print(sum)

#to print i value is not equal 0 and sum value is >500
i=int(input("enter a value"))
sum=0
while i!=0:
    sum=sum+i
    if sum>500:
        break
    i=int(input("enter a value"))

print(sum)

#to print the values decreasing order
list1=[0,1,2,3,4,5,6,7,8,9]
i=len(list1)-1
while i>=0:
    print(list1[i])
    i=i-1


list1=[0,1,2,3,4,5,6,7,8,9]
i=0
while i<=10:
  print(list1[i])
  i=i+1 

#even numbers
i=2
while i <=100:
    print(i)
    i=i+2


#to skip 50 and  continue to 100
a=5
while a<=100:
    if a==50:
        a=a+5
        continue
    print(a)
    a=a+5

a=5
while a<=100:
    if a==50:    
        break#if we use break it will print 5 to 45
    print(a)
    a=a+5

s=1
while s<=30:
    if s==20:
      s=s+1
      continue
    print(s)
    s=s+1


#to sum the numbers and stop while the 0 value will enter
i=int(input("enter a value"))
sum=0
while True:
    if i==0:
        break
    sum=sum+i
    i=int(input("enter a value"))
print(sum)


#create a list and stop while the 0 value will enter
list1=[]
value=input('enter data')
while value!='0':
    list1.append(value)
    value=input('enter data')
print(list1)

#write a python function that takes a list and returns a new list which distinct elements from the first list

samplelist=[1,2,3,3,3,3,4,5]
#uniquelist=[1,2,3,4,5]
{1,2,3,3,3,3,4,5}
set(samplelist)









