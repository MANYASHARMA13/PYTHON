#Q1
print('Q1')
x = int(input('Enter a number:'))
print('Binary equivalent of number is:', bin(x))
#Q2
print('Q2')
choice = input('''
Please select the type of operation you want to perform:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
if choice == '+':
           print('{}+{}'.format(num1,num2),num1+num2)
elif choice =='-':
           print('{}-{}'.format(num1,num2),num1-num2)
elif choice=='*':
           print('{}*{}'.format(num1,num2),num1*num2)
elif choice== '/':
           print('{}/{}'.format(num1, num2),num1/num2)
else: print('This operator is not valid.')
#Q3
print('Q3')
import math
#a
print('Q3(a)')
print('The answer to (3+4)*5 is:',(3+4)*5)
#b
print('Q3(b)')
n= int(input('Enter Number:'))
ans = (n*(n-1))/2
print('(n*(n-1))/2 is:',ans)
#c
print('Q3(c)')
r= int(input('Enter number:'))
m = 4*math.pi*(r**2)
print('4*math.pi*(r**2)is:',m)
#d
print('Q3(d)')
r_1 = int(input("Enter Number:"))
a = int(input("Enter Angle in degrees for cos:"))
b=int(input("Enter Angle in degrees for sin:"))
c = math.cos(a*math.pi/180)**2
d = math.sin(b*math.pi/180)**2
answer = (r_1*c + r_1*d)**0.5
print('The value of (r_1*c + r_1*d)**0.5 is:', answer)
#e
print('Q3(e)')
y1 = int(input("Enter Number y1:"))
y2 = int(input("Enter Number y2:"))
x1 = int(input("Enter Number x1:"))
x2 = int(input("Enter Number x2:"))
ansr = (y1 - y2)/(x1 - x2)
print('The value of (y1 - y2)/(x1 - x2) is:', answer)
print('Q4')
#Q4
for i in range(5):
    print(i)
print('--------')
for i in range (3,10):
    print (i)
print('---------')
for i in range (4,13,3):
    print(i)
print('---------')
for i in range (5,3,-1):
    print(i)
print('Q5')
#Q5
x= int(input('Enter the number of hydrogen atoms:'))
y= int(input('Enter the number of oxygen atoms:'))
z= int(input('Enter the number of carbon atoms:'))
h= 1.00794
c= 12.0107
o= 15.9994
weight = x*h+y*o+z*c
print('The weight of the carbohydrate is:',weight)
