#q1 
print('Q-1')
python='Python is a case sensitive language'
print(python)
print('Length of the string=',len(python))
# reversing 
print('Reversed order of the string=',python[::-1])
#storing-'a case sensitive' in a new string
slice=python[10:26]
print('New string containing-"a case sensitive"=',slice)
#replacing 
print('Replacing "a case sensitive" with "object oriented"')
new=python.replace("a case sensitive","object oriented")
print(new)
#finding index of a
index=python.find("a")
print('Index of "a"=',index)
#removing white spaces in string 
print('Removing all the white spaces in the string=',python.replace(" ",""))

#q2 string formatting
print('Q-2')
name='Manya Sharma'
sid=21102029
dept='Civil engineering'
cgpa=9.9
print("Hey,%s Here!"%(name))
print("My SID is %d"%(sid))
print("I am from %s department and my CGPA is %s" %(dept,cgpa))

#q3 bitwise operators
print('Q-3')
a=56
b=10
print("a=",a,"b=",b)
print('Part A) a&b=',a&b)
print('Part B) a|b=',a|b)
print('Part C) a^b=',a^b)
print('Part D) left shift a with 2 bits=',a<<2)
print('Part D) left shift b with 2 bits=',b<<2)
print('Part E) right shift a with 2 bits=',a>>2)
print('Part E) right shift b with 4 bits=',b>>4)

#q4 substring in string
print('Q-4')
x=input('Enter string-')
print('Is "name" present in the input string:')
if 'name' in x:
    print("YES")
else:
    print("NO")
    
#q5 sides of a triangles
print('Q-5')
a = float (input("Enter the length of first side:"))
b = float (input("Enter the length of second side:"))
c = float (input("Enter the length of third side:"))

x = int (a)
y = int (b)
z = int (c)

d = x+y>z
e = y+z>x
f = z+x>y

answer = str ( d & e & f)
answer = answer.replace ("True","yes")
answer = answer.replace ("False","no")
print('Can you form a triangle-',answer)
#q6 number of bits needed to be flipped to convert 'a' to 'b'
print('Q-6')

a= int(input("Enter the number 'a' :"))
b= int(input("Enter the number 'b' :"))
c= bin (a^b)

count=0
for i in c [2::]:
  if i=="1":
    count=count+1

print("The number of bits needed to be flipped to convert 'a' to 'b' are:",count)





    
