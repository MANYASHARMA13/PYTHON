#Q1
print('Q1')
marks=int(input('Enter the marks:'))
if marks>80:
    print('Your grade is A')
elif 60<marks<80:
    print('Your grade is B')
elif 50<marks<60:
    print('Your grade is C')
elif 45<marks<50:
    print('Your grade is D')
elif 25<marks<45:
    print('Your grade is E')
else:
    print('Your grade is F')

#Q2
print('Q2')
year=int(input('Enter the year:'))
if year%4==0:
    print('The year is a leap year')
elif year%400==0:
    print('The year is a leap year')
elif year%100==0:
    print('The year is not a leap year')
else:
    print('The year is not a leap year')

#Q3
print('Q3')
from random import randint

question = 1

while question<11:
    a = randint(0,20)
    b = randint(0,20)

    print('The question is ',a, '*',b)
    x= int(input('Enter your answer : '))

    if x == a*b:
        print ('Right!')
    else:
        print('Wrong! The answer is', a*b)
    question = question+1

else:
    print ('The game is over')
print('Q4')
for candies in range (200):
    if candies%5==2:
        if candies%6==3:
            if candies%7==2:
                print('Total candies in the bowl are:',candies)

