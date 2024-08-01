#if loop

#if
#else
#elif
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


#write a python function that checks weather a passed string is a palindrome or not

a=input('enter the password')
if a==a[::-1]:#reverse method 
    print("ok")
else:
    print('incorrect')
    