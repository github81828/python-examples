#write a python function that takes a list and returns a new list which distinct elements from the first list
#samplelist=[1,2,3,3,3,3,4,5]
#uniquelist=[1,2,3,4,5]


samplelist=[1,2,3,3,3,3,4,5]
list2=[]
for value in samplelist:
  if value not in list2:
      list2.append(value)
print(list2)
      
#write a python function that checks weather a passed string is a palindrome or not

a=input('enter the password')
if a==a[::-1]:#reverse method 
    print("ok")
else:
    print('incorrect')


#write a python function to check weather a no.falls within a given range

    
i=int(input('enter the number'))
if i in range(100):
    print('true')
else:
    print('false')


#write a python function that accepts a string and counts the no. of upper and lower case letters

a=input('enter a string')
for value in a:
    if value.islower():
        print(value)


#to print sum of the list
list1=[1,2,3,4,5,6,7,8,9]
sum=0
for variable in list1:
    sum=sum+variable
print(sum)


#????????
#CREATE A LIST TO STORE THE NAMES OF COLORS AND RETURN SIZE OF LIST
list1=['red','green','blue']
len(list1)

#CREATE A LIST FIND THE GREATEST AND MIMIMUM VALUE FROM THE LIST
list1=[100,200,300,400]
max(list1)
min(list1)

#CREATE A LIST & SHUFFLE THE ELMENTS IN RANDOM MANNER
import random
LIST1=[1,2,3,4,5,6,]
random.shuffle(LIST1)
LIST1

#CREATE A LIST AND FIND SUM OF ALL ELEMENTS OF A LIST ......... PENDING

#WRITE A PGM TO CREATE A LIST WITH ELEMNTS 1,2,3,4 ,5.DISPLAY EVEN ELEMETS OF THE LIST
LIST1=[1,2,3,4,5]
LIST1[1::2]

#WRITE A PGM TO ASSIGN GRADES TO STUDENTS AND DISPLAY ALL THE GRADES USING KEYS() AND GET() METHOD OF A DICTIONARY
students={'anu':'a','sanu':'b','manu':'c'}
print(students)
students.keys()
students.values()
students.get('anu')

#write a python pgm to get maximum and minimum values of a dictionary
marks={'anu':30,
       'manu':40,
       'sanu':500,
       'rinu':25}
max(marks)
min(marks)

#write a pp to sort a given dictionary by key
mylist={'a':1,
        'b':2,
        'c':3,
        'd':4}

sorted(mylist.keys())

#write a pp to map 2 list in a dictionary
anu=[1,2,3]
sanu=[100,200,300]
dictionary=dict(zip(anu,sanu))
print(dictionary)

#write a pp to find all keys in a dictionary
mylist={'a':1,
        'b':2,
        'c':3,
        'd':4}
print(mylist.keys())

#write a pp to create an intersection of sets 
a={1,2,3,4,5}
b={3,2,1,100,200}
print(a.intersection(b))

#write a pp to create union of sets
a={1,2,3,4,5}
b={3,2,1,100,200}
print(a.union(b))

#write a pp to create set difference
a={1,2,3,4,5}
b={3,2,1,100,200}
print(a.difference(b))

#write a pp to create a symmetric difference
a={1,2,3,4,5}
b={3,2,1,100,200}
print(a.symmetric_difference(b))

#write a pp to check if a set is a subset of another set
a={1,2,3,4,5}
b={3,2,1,100,200}
print(a.issubset(b))

#write a pp to create a shallow copy of sets
a={1,2,3,4,5}
b={3,2,1,100,200}
c=a.copy()
d=a#now here a and d is same member 

#write a pp to remove all elements from a goven set
a={1,2,3,4,5,100,200}
a.clear()

#write a pp to find the length of a set
a={1,2,3,4,5,100,200}
(len(a))

#write a pp to check if a given value is present in a set or not

a={1,2,3,4,5}
b={3,2,5,15,25}
(a.issubset(b))

#write a pp to remove the intersection of a second set with a first set

set1={1,2,3,4,5}
set2={3,2,5,15,25}
set1.difference_update(set2)

#create a list by picking an odd-items from the first list and even index items from the second
#l1=[3,6,9,12,15,18,21]
#l2=[4,8,12,16,20,24,28]

l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
odditems=l1[1::2]
odditems

evenitems=l2[0::2]
evenitems

l3=odditems+evenitems
l3

#remove and add item in a list ,write a pgm to remove the item prsent at index 4 and add it to the 2nd 
# position and atbthe end of the list
#l1=[34,54,67,89,43,94]remove index 4
#l2=[34,54,11,67,89,43,94]add element at index 2
#add elmnt at last 

l1=[34,54,67,89,43,94,]
l1.remove(89)
l1

l2=[34,54,11,67,89,43,94]
l2.insert(2,(11))
l2

l3=[34,54,11,67,89,43,94]
l3.insert(7,(11))#or append
l3

#slice list into 3 equal chunks and reverse each chunk and reverse each chunk
#sample_list=[11,45,8,23,14,12,78,45,89]

chunk1=[11,45,8,23,14,12,78,45,89]
chunk1[0:3]

chunk11=chunk1[0:3]
chunk11.reverse()
chunk11

chunk2=[11,45,8,23,14,12,78,45,89]
chunk2[3:6]

chunk21=chunk2[3:6]
chunk21.reverse()
chunk21

chunk3=[11,45,8,23,14,12,78,45,89]
chunk3[6:10]

chunk31=chunk3[6:10]
chunk31.reverse()
chunk31

#creat a python set such that it shows the element from both lists in a pair
first_list=[2,3,4,5,6,7,8]
second_list=[4,9,16,25,36,49,64]

l1=set(zip(first_list,second_list))
l1

#find the intersection of 2 sets (common) and remove those elmnts from the first set 
first_list={23,42,65,57,78,83,29}
second_list={57,83,29,67,73,43,48}

first_list.intersection(second_list)
first_list.difference_update(second_list)
first_list

#check if one set is a subset or superset of another set.if found ,delete all elmnts from that set 
first_list={27,43,34}
second_list={34,93,22,27,43,53,48}
first_list.issubset(second_list)
second_list.issubset(first_list)

first_list.issuperset(second_list)
second_list.issuperset(first_list)

first_list.clear()
first_list

second_list.clear()
second_list


#remove duplicates from a list and create a tuple and find the min and max number
samplelist=[87,45,41,65,94,41,99,94]
a=set(samplelist)#convert in to set so duplicates will remove
a
a=tuple(a)
a
min(a)
max(a)


#write a pp to multiply all the items in a list.......

#write a pp to clone or copy a list
l1=[1,2,3,4]
l2=[2,3,5]

l1=l2.copy()
l1

#write a pp to access index of a list
mylist=['anu','manu','sanu','rinu']
mylist.index('manu')

#write a pp to append a list to the second list

list1= [1,2,3,4]
list2=['anu','manu','sanu','rinu']

list2.append(list1)
list2

#write a pp to get the frequency(len) of elements in a list
list1= [1,2,3,4]
len(list1)

#removing empty strings from list
list1=['mike','','emma','kelly','','brad']
res=list(filter(None,list1))
res

#nested list
list1=[10,20,[300,400,[5000,6000],500,],30,40]
list1[0]
list1[2]
list1[3]
list1[2][2][1]
list1[2][0]
list1[2][2][1]=7000
list1
#to add 5000 next to 7k
list1[2][2].append(6000)
list1

list1=['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
sublist=['h','i','j']



#if loop

#if
#else
#elif
if (b>a):
    print('b is greater than a')
a=12
b=12
if (b>a):
    print('b is greater than a')
else:
    print('a is greater')
a=678
b=678
if (b>a):
    print('b is greater')
elif (a>b):
    print('a is greater')
a=3
b=3
if b>a:
    print("b is greater" )
elif a>b:
    print('a is greater')
else:
    print('a equal to b')
grades=70
if(grades>=70):
    print('graduated')
else:
    print('failed')

mark=int(input('enter your marks :'))
if(mark>80):
    print('grade is A')
elif(mark>70):
    print('grade is B')
elif(mark>60):
    print('grade is C')
elif(mark>40):
    print('grade is D')
else:
    print('failed')

a=int(input('enter a number'))
type(a)
age=int(input('enter your age'))
if(age<18):
    print('not eligible')
else:
    print('eligible')

a=5
b=26
b%a
b//a

number=int(input('enter a number'))
if(number%2==0):
    print('it is even')
else:
    print('it is odd')

unit=int(input('enter a unit:  '))
if(unit<=100):
    print('no charge is applicable')
elif(unit>100 and unit<=200):
    unit=(unit-100)*5
    print(unit)
else:
    unit=(unit-200)*10+500
    print(unit)



#?
#pg to display last digit of the no.
number=int(input('enter a number '))
print("last number ",number%10)

#pgm to check weather the last no. is divisible by 3 0r not
number=int(input('enter a number '))
if(number%3==0):
    print('it is divisible by 3')
else:
    print('it is not divisible by 3')

#pgm to accept a no. from 1-7 and display the name of the day like 1 for sunday .2 for monday and soon
number=int(input('enter a number between 1-7 '))
if(number==1):
    print('sunday')
elif(number==2):
    print('monday')
elif(number==3):
    print('tuesday')
elif(number==4):
    print('wednday')
elif(number==5):
    print('thursday')
elif(number==6):
    print('friday')
else:
    print('saturday')

#pgm to accept a no. from 1-12 and display name of the month and days in that month like 1 for janu.. and no. of days
#31 and so on 

number=int(input('enter a number between 1-12 '))
if(number==1):
    print('january')
elif(number==2):
    print('february')
elif(number==3):
    print('march')
elif(number==4):
    print('april')
elif(number==5):
    print('may')
elif(number==6):
    print('june')
elif(number==7):
    print('july')
elif(number==8):
    print('august')
elif(number==9):
    print('september')
elif(number==10):
    print('october')
elif(number==11):
    print('november')
else:
    print('december')

#accept any city from the user and display momument of that city
#city        delhi,agra,jaipur
#monument    redfort,tajmahal,jalmahal

city=input('travelled city ')
if(city=='delhi'):
    print('monument of delhi-redfort')
elif(city=='agra'):
    print('monument of agra-tajmahal')
else:
    print('monument of jaipur-jalmahal')

  #pgm to accept cost price of a bike and displAY the road tax tobe according to the following criteria....pen

costprice=int(input('enter the costprice'))


    #pgm tom checke no.is divisible by 7 or not
number=int(input('enter the number'))
if(number%7==0):
    print('it is divisible by 7')
else:
   print('it is not divisible by 7')

#pgm to display 'hello' if a no. entered by user is a multiple of 5 other wise print 'bye'

number=int(input('enter the number'))
if(number%5==0 ):
    print('hello')
else:
    print('bye')

#accept the percentage from the user and display the grade according to the following criteria 
#below 25 d
#25 to 45  c
#45 to 50  b
#50 to 60  c+
#60 to 80 A
#above 80  a+
percentage=int(input('enter the percentage'))
if(percentage<25):
    print('grade D')
elif(percentage>25 and percentage<45):
    print('grade C')
elif(percentage>45 and percentage<50):
   print('grade B') 
elif(percentage>50 and percentage<60):
    print('grade B+') 
elif(percentage>60 and percentage<80):
    print('grade A') 
else:
    print('grade A+')


#a company decide to bonus to employee according to the following criteria
#time period of service   and bonus

#more than 10 years     10%
#>=6 and <=10           8%
#less than 6 years      5%

# ask user for their salary and years of service and print net bonus amount

service=int(input('enter the service'))
salary=int(input('enter the salary'))
service=10
salary=10000
if(service>10):
    print((10/100)*salary)
elif(service>=6 and service<=10):
    print((8/10)*salary)
elif(service<10):
    print((5/10)*salary)

#accept the age ,sex('M,F'),no.of days and display the wages accordingly
age=int(input('enter the age'))
sex=(input('enter the sex (M,F)'))
numberofdays=int(input('enter the numberofdays '))
if(age>=18 and age<30) and sex=='M':
    print(numberofdays*700)
elif(age>=18 and age<30) and sex=='F':
    print(numberofdays*750)
elif(age>=30 and age<40) and sex=='M':
    print(numberofdays*800)
elif(age>=30 and age<40) and sex=='F':
    print(numberofdays*850)

#Accept the no.of days from the user and calculate the charge for library according to following
numberofdays=int(input('enter the numberofdays '))
chargeoflibrary=int(input('enter the charge'))
if(numberofdays<=5):
    print(chargeoflibrary*2)
elif(numberofdays>=6 and numberofdays<=10):
    print(chargeoflibrary*3)
elif(numberofdays>=11 and numberofdays<=15):
     print(chargeoflibrary*3)
elif(numberofdays<15):
    print(chargeoflibrary*5)


#accept the marked price from the user and calculate net amount as(marked price-discount)to pay according to following criteria
markedprice=int(input('enter the marked price'))
markedprice=5000
if markedprice>10000:
    print ("netprice=",markedprice-((20/100)*markedprice))
elif(markedprice>7000 and markedprice<=10000):
    print("netprice=",markedprice-((15/100)*markedprice))
elif(markedprice<=7000):
    print("netprice=",markedprice-((10/100)*markedprice))

#accept the following from the user and calc the percentage of class attended 
#a   total no.of working days
#b   total no.of days for absent
#after calculating percentage show that,if the percentage is less than 75 than student will not be able to sit in exam
total_days=int(input('enter the number of working days'))
absents=int(input('enter the no of abscents'))
percentage=(total_days-absents)/total_days*100
if percentage<75:
    print('student will not be able to sit in exam')
elif (percentage>75):
    print('student will be able to sit in exam')


#for loops#############################################  

list1=[1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)


list1=[1,2,3,4,5,6,7,8,9,10,11,12]
for index in range(0,len(list1)):
    print(list1[index])

    #print even numbers from the list

    for num in list1:
        if num%2==0:
            print(num)

for num in list1:
    if num %2==0:
        print('even number',num)
    else:
        print('odd number',num)

#start sum at zero
list_sum=0
for num in list1:
    list_sum=list_sum+num
print(list_sum)

#start sum at zero
list_sum=0
for num in list1:
  list_sum+=num
print(list_sum)


for letter in 'This is a string.':
    print(letter)

    #loop in tuple

    tup=(1,2,3,4,5)
    for t in tup:
        print(t)


list2=[(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

    #now with unpacking

for(t1,t2) in list2:
    print(t1,t2)




d={'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)


#create a dictionary view object
d.items()

dict_items ([('k1',1),('k2',2),('k3',3)])


#dictionary un packing
for k,v in d.items():
    print(k)
    print(v)

#create a list to get duplicates
jenny=[1,1,2,2,3,3,3,4,4,5,5,5,6,7,8,9,10]
a=set(jenny)
a#not correct


#print non dupicates 
jenny=[1,1,2,2,3,3,3,4,4,5,5,5,6,7,8,9,10]
jacob=[]
for number in jenny:
    if jenny.count(number)==1:
        jacob.append(number)
jacob



jenny=[1,1,2,2,3,3,3,4,4,5,5,5,6,7,8,9,10]
jacob=[]
for number in jenny:
    if jenny.count(number)in[1,2]:# in membership operator
        jacob.append(number)
jacob
set(jacob)


print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high, Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t\t\t How I wonder what you are")



