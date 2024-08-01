list1=[1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)

for i in range(5):
    print(i)

#to print even numbers
for i in range(0,20,2):
    print(i)

#to print 100 numbers
for i in range(100):
    print(i)

sum=0
for i in range(10):
    sum=sum+i
print(sum) 

#will show each number square
numbers=[1,2,3,4,5]
for i in numbers:
    square=i**2
    print( square)

#will show total square
numbers=[1,2,3,4,5]
for i in numbers:
    square=i**2
print( square)

#Exercise 1: Print First 10 natural numbers using for loop
for i in range(1,11):
    print(i)

#Exercise 1: Print First cube of first 5  natural numbers using for loop
numbers=[1,2,3,4,5]
for i in numbers:
    cube=i**3
print(cube)

#?display numbers from a list using loop
list1=[10,20,30,40,1,2,3]
for num in list1:
    print(num)

#python for loop to iterate through the letters in a word
name=input('enter a name ')
for i in name:
    print(i)

for i in "malayalam":
    print(i)

#?print list in reverse order using a loop
letters=['a','b','c','d']
letters.reverse()
letters
#letters[::-1]
for i in letters:
    print(i)
#method2
list1=[1,2,3,4,5]
size=len(list1)-1
for i in range(size,-1,-1):
    print(list1[i])

#display numbers from -10 to -1 using for loop
for i in range(-10,0,1):
    print(i)

#use a loop to display elements from a given list present at odd index positions
list1=[0,1,2,3,4,5,6,7,8,9,10]
for num in list1[1::2]:
    print(num)

#python for loop to iterate through the letters in a word
for i in 'python':
    print(i)

#python for loop to iterate through list
list1=['cat','rat','rabbit']
for i in list1:
    print(i)

#python for loop to find sum of all numbers in a list
list1=[1,2,3,4,5,6]
sum=0   #giving a value to sum
for i in list1:
    sum=sum+i
    print(sum)

#python for loop to print a triangle of stars
# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")

#python for loop to find the minimum element in a list
list1=[1,2,3,4,5,6]
for i in list1:
    print(min(list1))

#python for loop to print the multiples of 3 using range()function

for i in range(30)[::3]:
    print(i)


#write a python function that takes a list and returns a new list which distinct elements from the first list
#samplelist=[1,2,3,3,3,3,4,5]
#uniquelist=[1,2,3,4,5]


samplelist=[1,2,3,3,3,3,4,5]
list2=[]
for value in samplelist:
  if value not in list2:
      list2.append(value)
print(list2)
      

    #to print sum of the list
list1=[1000,2000]
sum=0
for variable in list1:
    sum=sum+variable
print(sum)







