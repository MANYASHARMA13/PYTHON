print('Python Assignment 1')
#Q1
print('Q1')
x= float(input('Enter the first number:'))
y= float(input('Enter the second number:'))
z= float(input('Enter the third number:'))
average = (x+y+z)/3
print('The average of the numbers is:',average)
#Q2
print('Q2')
g= float(input('Enter gross income:'))
d= int(input('Enter number of dependents:'))
x= g-10000-(3000)*d
y= x*0.2
print('The tax is:$',y)
#Q3
print('Q3')
sid= int(input('Enter SID:'))
name= str(input('Enter name:'))
gender= str(input('Enter Gender:'))
course= str(input('Enter course name:'))
cgpa= float(input('Enter cgpa:'))
details= [sid,name,gender,course,cgpa]
print('Student',details)
#Q4
print('Q4')
a= float(input('Enter marks of student 1:'))
b= float(input('Enter marks of student 2:'))
c= float(input('Enter marks of student 3:'))
d= float(input('Enter marks of student 4:'))
e= float(input('Enter marks of student 5:'))
marks=[a,b,c,d,e]
marks.sort()
print('Sorted list of marks',marks)
#Q5
print('Q5')
list=['Red','Green','White','Black','Pink','Yellow']
print('color',list)
list.remove('Black')
print('Part A-List after removing fourth element\n',list)
list=['Red','Green','White','Black','Pink','Yellow']
del list[3:4]
list.insert(3,'Purple')
print('Part B- Replacing black and pink with purple\n',list) 

      



                  

         
               
