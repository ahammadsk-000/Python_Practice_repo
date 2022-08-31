##############################Basic Python##################################
'''# Python program starts with main function
def Main():
    print('Hello World!!!!')

if __name__ == '__main__':
    Main()'''

# to know total keywords
'''import keyword
print(keyword.kwlist)'''

''' # global variables
g=10
def see():
    print(g)
#see()


x=20
def see1():
    x=30
    print(x)
#print(x)
#see1()

x=50
def watch():
    global x
    x=90
    print(x)

watch()
print(x)'''

# local variables
'''def show():
    x = 20
    print(x)
show()
print(x)'''

# non local variables
'''def outer():
    x='local'

    def inner():
        nonlocal x #nonlocals are used in nested functions
        x='nonlocal'
        print(x)
    inner()
    print('outer :',x)
outer()'''


'''var= "James Bond"
print(var[2::-1])'''

'''l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
print(id(l1))
print(id(l2))'''

'''import keyword
p=10
def see():
    pass
print(keyword.iskeyword(p))'''

# type casting
#s=10
#d = str(s)
#print(type(d))
#d = float(s)
#print(type(d))
'''d=complex(s)
print(type(d))'''

'''d = range(s)
print(d)
print(type(d))'''

# to take multiple values from user
'''x,y = input('Enter the values: ').split(" ")
print(x,y)'''

'''x,y = [int(i) for i in input('Enter values:').split(" ")]
print(x,y)'''

'''x,y,z = [int(i) for i in input('Enter 3 values: ').split(" ",3)]
print(x,y,z)'''

'''a=10
b=20
c=30
d=50
print(a,b,c,d,sep='&')
print(a,b,c,d,end=' ')
print(d,c,b,a)'''

'''l=[1,2,3,4,5,6]
print(*l)'''

#print('hello'),print('hi')
'''a=(1,2,3,4,5)
b=(1,2,3,4,5)
print(id(a))
print(id(b))
location will be same if values are immutable'''

'''a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(id(a))
print(id(b))
location will be different if the values are mutable'''

# ternary operator
'''a=20
b=30
d = 'a is equals to b' if a==b else 'a is greater than b' if a>b else 'b is greater than a'
print(d)

f = 'True' if a<b else 'False'
print(f)'''

# operator overloading
'''class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,o):
        return self.a + o.a

b1 = A(1)
b2 = A(2)
print(b1+b2)'''

'''class A:
    def __init__(self,a):
        self.a = a
    def __add__(self, other):
        return self.a+other.a

obj1 = A(10)
obj2 = A(20)
obj3 = A('Hello')
obj4 = A('World')
print(obj1+obj2)
print(obj3+obj4)'''

'''class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a+other.a+self.b+other.b

obj1 = A(10,20)
obj2 = A(30,40)
print(obj1+obj2)'''


'''class A:
    def __init__(self,a):
        self.a = a
    def __gt__(self, other):
        if self.a>other.a:
            return True
        else:
            return False

obj1 = A(10)
obj2 = A(20)
print(obj1>obj2)'''


'''class A:
    def __init__(self,a):
        self.a = a
    def __lt__(self, other):
        if self.a< other.a:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.a == other.a:
            return True
        else:
            return False
obj1 = A(10)
obj2 = A(20)

if (obj1<obj2):
    print('obj1 is less than obj2')
else:
    print('obj1 is greater than obj2')

obj3 = A(10)
obj4 = A(10)

if (obj3 == obj4):
    print('obj3 is equal to obj4')
else:
    print('obj3 is not equal to obj4')'''


'''class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return m1+m2


s1 = Student(20,40)
s2 = Student(60,70)
s3 = s1+s2       #Student.__add__(s1,s2)
print(s3)'''


'''class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3


s1 = Student(20,40)
s2 = Student(60,70)
s3 = s1+s2       #Student.__add__(s1,s2)
print(s3.m1)
print(s3.m2)'''

# __new__(cls) method
'''class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print('__init__ magic method is called')
        self.name = 'Satya'
emp = Employee()'''

'''class Employee:
    def __new__(cls):
        print("new method called")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print("init method is called")
        self.name = 'Satya'

emp = Employee()
print(emp.name)'''

# __str__() method
'''s=12
print(type(str(s)))
d = int.__str__(s)
print(type(d))'''

'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return 'My name is '+self.name+' and my salary is '+self.salary

e = Employee('Syam','70000')
print(e)'''

# operator functions
'''import operator
a=2
b=5
print(operator.add(a,b))
print(operator.mul(a,b))
print(operator.mod(a,b))
print(operator.truediv(a,b))
print(operator.lt(a,b))'''

'''import operator as op
l=[1,2,3,4,5,6,7,8,9,10]
l2=[444,33,222,555]
op.setitem(l,0,330)
print(l)
op.delitem(l,0)
print(l)
f = op.concat(l,l2)
print(f)'''

# Encoding()
'''a="GeeksforGeeks"
c = b'GeeksforGeeks'
d = a.encode()
if c==d:
    print('Encoding successful')
else:
    print('Encoding is not successful')'''
# Decoding
'''a='GeeksforGeeks'
c=b'GeeksforGeeks'
d= c.decode()
if a == d:
    print("Decoding is successful")
else:
    print('Decoding is not successful')'''

# type conversion from char ti int and int to char
'''a='A'
d = ord(a)
print(d)

a=65
d = chr(a)
print(d)'''

# String operations #
'''S = 'String'*5
print(S)'''

'''s1 = 'Hello '
s2 = 'World'
s3 = s1+s2
print(s3)'''


'''s='abcdefghijklmnopqrstuvwxyz'
d = s[5:10]
print(d)

s='abcdefghijklmnopqrstuvwxyz'
d = s[5:10:2]
print(d)

s='abcdefghijklmnopqrstuvwxyz'
print(s[::-1])

s='abcdefghijklmnopqrstuvwxyz'
print(s[5::-1])'''

# string formatting
# String modulus formatting method
'''a=10
f1=5.9
s = 'Hello i am ali my num is %d my height is %f '%(a,f1)
print(s)

s1 = 'Hello this is %(name)s and my phone num is %(phnum)d'%{'name':'Ahammad','phnum':67676767}
print(s1)

s2 = 'Hello this is %(name)s and my age is %(age)d '%({'name':'Ali','age':50})
print(s2)

s3 = '%8d'%(20)
print(s3)

s4 = '%08d'%(20)
print(s4)

s5 = '%f'%(42.78998)
print(s5)

s6 = '%.3f'%(42.78998)
print(s6)

s7 = '%f'%(42.78998)
print(s7)'''

# format method
'''a=10
b='Ahammad'
s = 'My name is {} and my num is {}'.format(b,a)
print(s)

s1 = 'My name is {1} and my num is {0}'.format(a,b)
print(s1)

s2 = 'My company is {name} and my salary is {salary}'.format(name='Accenture',salary=23000)
print(s2)

s3 = '{0:d}'.format(10)
print(s3)

s4 = '{1:d}'.format(40,50)
print(s4)

s5 = '{1:5d}'.format(40,50)
print(s5)

s6 = '{1:05f}'.format(40,50.089878)
print(s6)

s7 = '{1:05.2f}'.format(40,50.089878)
print(s7)

s8 = '{0:<5d}'.format(23)
print(s8)

s9 = '{0:>5d}'.format(23)
print(s9)

s10 = '{0:#>5d}'.format(23)
print(s10)

s11 = '{0:@^5d}'.format(23)
print(s11)

s12 = '{num:05d}'.format(num=23)
print(s12)

s12 = '{num:8f}'.format(num=23.678)
print(s12)

s13 = '{num:8.3f}'.format(num=23.678676)
print(s13)

s14 = '{num:08.3f}'.format(num=23.678676)
print(s14)

s15 = '{num:*<8.3f}'.format(num=23.678676)
print(s15)

s16 = '{num:*>8.3f}'.format(num=23.678676)
print(s16)

s16 = '{num:*^8.3f}'.format(num=23.678676)
print(s16)

s16 = '{num:.3s}'.format(num='Rayudu')
print(s16)'''

# f-string method:
'''a=50
s = f'hello this is my num {a}'
print(s)


s1 = f'hello this is my num {a:5d}'
print(s1)

s2 = f'hello this is my num {a:05d}'
print(s2)

s3 = f'hello this is my num {a:#<5d}'
print(s3)

s4 = f'hello this is my num {a:#<5d}'
print(s4)

s5 = f'hello this is my num {a:*>5d}'
print(s5)

s6 = f'hello this is my num {a:#^5d}'
print(s6)

a=90.9876
s7 = f'hello this is my num {a:8.3f}'
print(s7)

s8 = f'hello this is my num {a:*^8.3f}'
print(s8)

a='syampandu'
s9 =f'Hello this is my name {a:16s}'
print(s9)

a='syampandu'
s9 =f'Hello this is my name {a:#<16.3s}'
print(s9)

a='syampandu'
s10 =f'Hello this is my name {a:#>16.3s}'
print(s10)

a='syampandu'
s10 =f'Hello this is my name {a:#^16.3s}'
print(s10)'''

# string escape sequence
'''a='hi hello \"how are you\"'
print(a)
a1=r'hello "how are you" i am fine'
print(a1)'''

# String built-in functions
'''import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)

s='hello'
print(s.isprintable())
s1='hello this is my world'
print(s1.title())

s1='hello this is my world'
print(s1.islower())

s1='hello this is my world'
print(len(s1))
print(s1.endswith('world',17,22))

s1='hello this is my world'
print(s1.startswith('hello',0,5))

s1 = '763736536'
print(s1.isdigit())

s1='abcdefjgdgdhgd'
print(s1.isalpha())

s1='hfjvhfr7etryetye4343'
print(s1.isalnum())

s1='54635643564'
print(s1.isdecimal())

s1='345364536gchdghgd'
print(s1.index('3',1,10))

s1='degdhgeefegded'
print(s1.upper())
print(s1.isupper())

s1='HGDJFEFEFEFEFE'
print(s1.swapcase())

s1='hello this is jython tutorial'
r= s1.replace('jython','python')
print(r)

s1='Hello This Is Magic'
print(s1.istitle())

s1='abcde'
print(s1.isidentifier())

s1='gggvhjfhvf'
print(len(s1))

s1='hello2345hellodfhejjrookkk'
print(s1.rindex('o',0,25))

s1='g5635635fggwgdgw'
print(max(s1))
print(min(s1))

s1='Welcome everyone to\rthe world of Geeks\nGeeksforGeeks'
print(s1.splitlines())

s1='welcome First Chapter of Science'
print(s1.capitalize())

s1='i\tlove\tgfg'
print(s1.expandtabs(20))

s1='hello this is not for is ot for time pass'
print(s1.find('is'))

s1='hello this is not for is ot for time pass'
print(s1.rfind('is'))

s1='hello this is not for is ot for time pass'
print(s1.count('is',0,20))

s1='GCGEHGHEGHFGEF'
print(s1.lower())

s1='gdhvgwh@jjgvwhjgvw@hghcgdhcdh'
print(s1.split('@',1))

s1='gdhvgwh@jjgvwhjgvw@hghcgdhcdh'
print(s1.split('@',2))

s1='gdhvgwh@jjgvwhjgvw@hghcgdhcdh'
print(s1.rsplit('@',2))

s1='gdhvgwh@jjgvwhjgvw'
print(s1.rpartition('@'))

s1='gdhvgwh@jjgvwhjgvw'
print(s1.partition('@'))

s1='hello # this  is not magic'
h = s1.partition("#")
print(list(h))

s='helloworldthisisnotgood'
s1= '-'.join(s)
print(s1)

s1='                hello                 '
print(s1.strip())

s1='           hello'
print(s1.lstrip())

s1='hello                  '
print(s1.rstrip())

s1='helloh'
print(s1.strip('h'))

#mapping in string translation

table={119 : 103, 121 : 102, 117 : None }
s1='weeksyourweeks'
d= s1.translate(table)
print(d)

#Another method providing mapping using maketrans
str1='wy'
str2='gf'
str3='u'
trg='weeksyourweeks'

table=trg.maketrans(str1,str2,str3)
d = trg.translate(table)
print(d)

s='hello'
print(s.rjust(10,'#'))

s='hello'
print(s.ljust(10,'#'))

s='hello'
print(s.center(10,'#'))

s='hello'
print(s.zfill(10))

s='hello world'
d= ''.join(reversed(s))
print(d)

a='dog'
b='dog'
print(id(a))
print(id(b))

string = 'Hello 1 World 2'
vowels = ('a','e','i','o','u')

d = ''.join([i for i in string if i not in vowels])
print(d)'''

# String operations
'''for i in range(5):
    s = input('Enter ur name: ')
    print(s)'''

'''a='refrigerator'
count=0
for i in a:
    count +=1
print('length of :',a,' is : ',count)'''

'''a='This is orange juice'
d = 'orange' in a
print(d)'''


'''a = 'Hello, World'
d1 = a.find('o')
d2 = a.rfind('o')
d3 = a.find(',')
d4 = a.rfind(',')
print('for /"O/" ',d1,d2)
print('for /",/" ',d3,d4)'''

'''a= "Robert Brett Roser"
s = a.split(" ")
name = s[0][0]+'.'+s[1][0]+'.'+s[2]
print(name)'''

'''a= "This is umbrella"
s = a.count('e')
s1 = a.count('is')
print(s)
print(s1)'''

'''a= "Hello, have a good day"
vowels = 'aeiou'
s=''
for i in a:
    if i not in vowels:
        s +=i
print(s)'''

'''str=input("Enter any String :")
d = str.split(" ")
print(list(d))
l=[]
for i in d:
    count = len(i)
    l.append(count)
print(l)
ma = max(l)
r = len(l)
for i in range(r):
    if l[i] == ma:
        print('The heighest ength of word is: ', d[i])'''


'''str1 = input('Enter a string: ')
d = str1.upper()
print(d)'''

'''str1 = 'i am am am hello my my name'
d = str1.split(" ")
f = set(d)
f = list(f)
#print(f)
s = ' '.join(f)
print(s)'''


'''s = 'ajsajgaAHGHFHFFFJZz'
for i in s:
    print('The ascii value of : ',i,' is: ',ord(i))'''

'''s = 'hello this is not my life'
d = s.replace(' ','#')
print(d)'''

'''s1 = input('Enter first value: ')
s2 = input('Enter second value: ')
s1 = s1.lower()
s2 = s2.lower()
s1 = s1.split(" ")
s2 = s2.split(" ")

for i in s1:
    if i in s2:
        print(i)'''

"""str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub, 4))

myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(id(myString))
print(id(stringList[1]))

myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)"""


'''s1 = "Abc"
s2 = "Xyz"
s3=''
r= len(s1)
p = 0
k= -1
for i in range(r):
    s3 = s3 + s1[p]+s2[k]
    p +=1
    k -=1
print(s3)'''

'''s1 = "Yn"
s2 = "PYnative"

count =0
for i in s1:
    if i not in s2:
        count +=1
if count >0:
    print("not balanced")
else:
    print("balanced")'''


'''str1 = "Welcome to USA. usa awesome, isn't it?"
str1 = str1.lower()
s = str1.count('usa')
print(s)'''

'''str1 = "Apple"
d={}
for i in str1:
    if i not in d:
        d[i] =1
    else:
        d[i] = d[i]+1
print(d)

str1 = "PYnative"
print(str1[::-1])

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print(str1.rfind('Emma'))

str1 = 'Emma-is-a-data-scientist'
s = str1.split("-")
print(s)

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str1 = []
for i in str_list:
    if i:
        str1.append(i)

print(str1)

str1 = "/*Jon is @developer & musician"
str2 = ''.join([i for i in str1 if (i.isalpha() or i.isspace())])
print(str2)

str1 = 'I am 25 years and 10 months old'
d = ''.join([i for i in str1 if i.isdigit()])
print(d)

str1 = "Emma25 is Data scientist50 and AI Expert"
d = str1.split(" ")
counta=0
countd=0
l=[]
for i in d:
    for j in i:
        if j.isdigit():
            countd +=1
        if j.isalpha():
            counta +=1

    if counta >0 and countd >0:
        l.append(i)
    counta = 0
    countd = 0
print(l)

import string
str1 = '/*Jon is @developer & musician!!'

for char in string.punctuation:
    str1 = str1.replace(char,'#')

print(str1)'''

# List operations

'''l=[1,2,3,4,5]
a=l
l[0] = 10
print(a)'''

'''a= [1,2,3,4,5]
b = a.copy()
b[0] = 100
print(b)
print(a)
print(id(a))
print(id(b))'''

'''a=[1,2,3,4,5,6,7]
b = a[::]
print(b)
print(id(a))
print(id(b))'''

'''t = (1,2,3,4,5,6)
l = list(t)
print(l)
print(type(l))

l = list(range(0,5))
print(l)'''


'''a = [1,2,3,4,5]
b =a
print(b)
a[1]=2000
print(b)
print(a)'''

'''import copy
l1=[1,2,3,4,5]
l2 = copy.copy(l1)
print(l1)
print(l2)
l1[0] = 200
print(l1)
print(l2)
print(id(l1))
print(id(l2))

l1=[1,2,3,4,5]
l2 = copy.copy(l1)
l1.append(100)
print(l1)
print(l2)

l1=[1,2,3,4,5,[6,7,8,9,10],[1,2,3,4,5],[6,7,8,9,10]]
l2 = copy.copy(l1)
l1[5][0] = 2000
print(l1)
print(l2)
print(id(l1))
print(id(l2))'''

'''from copy import copy
l1 = [[1,2,3,4,5],[4,5,6,7,4]]
l2 = copy(l1)
l2[1][0] =1000
print(l1)
print(l2)
print(id(l1))
print(id(l2))'''

'''from copy import copy
l1 = [[1,2,3,4,5],[4,5,6,7,4]]
l2 = copy(l1)
print(l1)
print(l2)
l1.append([20,30,40,50])
print(l1)
print(l2)'''

# deep copy
'''from copy import *
l1 = [1,2,3,4,5]
l2 = deepcopy(l1)
l1[0] = 100
print(l1)
print(l2)

l1 = [1,2,3,4,5]
l2 = deepcopy(l1)
l2.append(30)
print(l1)
print(l2)

l1= [1,2,3,4,5,[6,7,8,9,10],[1,2,3,4,5],[6,7,8,9,10]]
l2 = deepcopy(l1)
l1[5][0] = 500
print(l1)
print(l2)'''

'''import functools
l=[1,2,3,4,5]
s = functools.reduce(lambda x,y: x+y,l)
print(s)

import functools
l=[1,2,3,4,5]
def add(x,y):
    return x+y
s = functools.reduce(add,l)
print(s)

import itertools
l=[1,2,3,4,5]
s = itertools.accumulate(l,lambda x,y: x+y)
print(list(s))

l=[1,2,3,4,5]
p = sum(l)
print(p)

l1=[1,2,3,4,5]
l2=[1,2,3,4,5,6,7]
print(max(l2))'''

# enumerate object
'''a = [1,2,3,4,5]
d = enumerate(a,start=0)
print(list(d))

for i,v in enumerate(a):
    print(i,v)'''

# filter() function

'''sequence = ['g','e','e','j','k','s','p','r']

def compare1(x):
    ov = ['a','e','i','o','u']
    if x  in ov:
        return x

d = filter(compare1,sequence)
print(list(d))'''

# map() function
'''a=[1,2,3,4,5]

def add1(x):
    return x+1
s = map(add1,a)
print(list(s))

s = map(lambda x: x+1,a)
print(list(s))'''

'''from functools import reduce

a=[1,2,3,4,5,6,7,8,9,10]
s = reduce(lambda x,y: x+y,a)
print(s)
print(sum(a))

d = reduce(lambda x,y: x if x>y else y,a)
print(d)'''

'''a= [10, 200, 300, 400, 500, 60, 70, 80, 90]

a[1:5] = []
print(a)

print(a[4:2:-1])
a= [10, 200, 300, 400, 500, 60, 70, 80, 90]
a.reverse()
print(a)
a.sort()
a.sort(reverse=True)
print(a)

a= [10, 200, 300, 400, 500, 60, 70, 80, 90]
d = reversed(a)
print(list(d))

List1 = [22, 24, 30, 22, 45, 67, 22, 30, 45]
item_to_remove = 22
f = List1.count(item_to_remove)
for i in range(f):
    List1.remove(item_to_remove)
print(List1)

List1 = ['ABC',[], 'xyz', 'abc',[], 'XYZ', []]
l=[]
for i in List1:
    if i :
        l.append(i)
print(l)


i = [[1, 2, 3], [4, 5], [6, 7, 8]]
l=[]
for j in i:
    l.extend(j)

print(l)

List1 = [10, 50, -40, 60, -30]

s = filter(lambda x: x>=0, List1)
print(list(s))

List1 = [10, 5, -4, 6, -3, 7, 9]
s1 = filter(lambda x: x%2==0,List1)
print('even',list(s1))
s2 = filter(lambda x: x%2!=0,List1)
print('odd',list(s2))'''

'''import random
l=[1,2,3,4,5,6,7]
s = random.choice(l)
print(s)'''

'''name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]

d = zip(name,animal,age)
print(list(d))'''

'''name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
r = dict(zip(name,animal))
print(r)

r = range(5,10)
print(list(r))'''

'''li1 = [2,3,4]
li2 = [2,4]
r = all(i%2==0 for i in li1)
e = all(i%2==0 for i in li2)
print(r)
print(e)


li1 = [1,2,3]
li2 = [1,3]
e = any(i%2==0 for i in li1)
r = any(i%2==0 for i in li2)
print(e)
print(r)

p= [1,2,3]
r = p*3
print(r)

p = ['a','b','c','d']
g = ' '.join(p)
print(g)

li = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
p = len(li)
for i in range(p):
    print(li[i][0])


li = ['blue', 'pink', 'green', 'green', 'yellow', 'pink', 'orange']
d={}
for i in li:
    if i not in d:
        d[i] = 1
    else:
        d[i] =d[i]+1
print(d)



li = [1,2,3,4,5,6,7,8,9,10]
f = [i for i in li if i%2==0]
print(list(f))

li = [10,1,9,2,8,3,7,4,6,5]
li.sort(reverse=True)
print(li)

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
del li[12:17]
print(li)


a = [10,20,30,40,50]
s = map(lambda x:x+10,a)
print(list(s))


a = [-10, 27, 1000, -1, 0, -30]
f = filter(lambda x: x>=0,a)
print(list(f))

from functools import reduce

numbers = [100,10,5,1,2,7,5]

def sub1(a,b):
    return a-b

d = reduce(sub1,numbers)
print(d)

li = ['a','b','c','d','e']
li.insert(3,'100')
print(li)

alphabet = ['a', 'b', 'c']
integers = [1, 2, 3]
f = list(zip(alphabet,integers))
print(f)

a = [10,20,30,40,50]
d = map(lambda x: x*5,a)
print(list(d))

li=[1,2,3,4,5]
print(5 in li)



my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

my_list.sort(key= lambda e: e['key']['subkey'],reverse=True)
print(my_list)

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
my_list.sort(key= lambda e: e['key']['subkey'],reverse=True)
print(my_list)

original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]

g = [ {k:v for k,v in d.items() if k !='key1'} for d in original_list]
print(g)


color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all(c=='green' for c in color1))
print(all(c=='green' for c in color2))

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)


Sample_list = [1,2,3,4]
string = 'emp'
l=[]
for i in Sample_list:
    d = string+str(i)
    l.append(d)
print(l)

l= [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
r = len(l)
for i in range(r):
    for j in range(r):
        if l[i]>l[j]:
            l[i],l[j] = l[j],l[i]

print(l)

num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
s = max(num,key=sum)
print(s)

s1=[10, 20, 30]
s2=[40, 50, 60]
print(s1+s2)

l1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l=[]
for i in l1:
    if i not in l:
        l.append(i)
print(l)

d = [{},{},{12,13}]
p = len(d)
count =0
for i in d:
    if not i:
        count +=1
if count == p:
    print('True')
else:
    print("False")'''


'''l = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
l1=[]
for i in l:
    if type(i) == int:
        l1.append(i)
    else:
        l1.extend(i)
print(l1)

l = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

l=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l2=[]
l3=[]
o = len(l)
for i in range(o):
    p=[l[i]]
    if l[i] not in l3:
        l3.append(l[i])
        for j in range(i,o):
            if l[i] ==l[j]:
                p.append(l[j])
        l2.append(p)
print(l2)'''

'''s= 'restart'
i = ''
for j in s:
    if j not in i:
        i +=j
    else:
        i +='$'

print(i)


l = 'abc'
s = 'xyz'
l,s = s[0:-1]+l[-1],l[0:-1]+s[-1]
print(l,s)

d1 = [10, 20, 30, 40, 50]
d2 = [1, 2, 3, 4, 5]
print( d1 - d1 )'''



'''list = ['a', 'b', 'c', 'd', 'e']
print(list[10:] )'''

'''import array
stu_roll = array.array('i',[1,2,3,6,4,5,6,6,6,6])
print(stu_roll)

stu_roll.append(20)
print(stu_roll)
stu_roll.insert(0,300)
print(stu_roll)
stu_roll.pop()
print(stu_roll)
stu_roll.pop(0)
print(stu_roll)
stu_roll.remove(6)
print(stu_roll)

f = stu_roll.index(6)
print(f)

s=array.array('i',[20,30,40,50])
stu_roll.extend(s)
print(stu_roll)

stu_roll.reverse()
print(stu_roll)

nw_arr = stu_roll[2:6:1]
print(nw_arr)'''

'''stu_f = array.array('f',[12.3,45.3,56.5,48.5])
print(list(stu_f))'''

'''str = 'My Name is Jessa'
l1 = len(str)
l=[]
s= ''
for i in range(l1):

    if str[i] != ' ':
        s += str[i]
    else:
        l.append(s)
        s = ''
    if i == l1-1:
        l.append(s)
l = l[::-1]
s1 =''
for i in l:
    s1 +=i+' '
print(s1)'''



'''str = 'My Name is Jessa'
l1 = len(str)
l=[]
s= ''
for i in range(l1):

    if str[i] != ' ':
        s += str[i]
    else:
        s = s[::-1]
        l.append(s)
        s = ''
    if i == l1-1:
        s = s[::-1]
        l.append(s)
#l = l[::-1]
s1 =''
for i in l:
    s1 +=i+' '
print(s1)'''

'''l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

n = len(l)
p=[10,20,30,40,50]
i=0
while i<n:

    if l[i] not in p:
        del l[i]
        i -=1
        n = len(l)
    i +=1
print(l)'''

'''dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
d={}
for i,v in dict.items():
    d[v] = i
print(d)'''


'''sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
l=[]
l1=[]
for i in sample_list:
    if i not in l:
        l.append(i)
    else:
        l1.append(i)
print('Unique elements: ',l)
print('Duplicate elements: ',l1)'''

'''d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
l1 = ['A', 'C', 'F']
d={}

for i,v in d1.items():
    if i in l1:
        d[i] = v
print(d)'''

'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
'''n=6
m=5
k=1
l=1
for i in range(1,n):
    print(i,end=' ')
    for j in range(1,m):
        print(k,end=' ')

    print()
    k +=1
    m -=1'''




'''def outer(x,y):
    def inner(x,y):
        return x+y
    z = inner(x,y)
    return z

x='Emma'
y = 'Kelly'

d = outer(x,y)
print(d)'''

'''list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
list1[1][2][2][1] = 3500

print(list1)'''

'''emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}

emp_dict['company']['employee']['payable']['increment'] = 200
print(emp_dict)'''


'''import array as arr
ar1 = arr.array('d',[1.4,3.4,5.6,7.6,9.8,5.4,3.2,8.6])
print(ar1[-5:])
print(ar1[5:])
print(ar1[:])
ar1.extend([6.5,7.8,9.0])
print(ar1)

ar1 = arr.array('d',[1.4,3.4,5.6,7.6,9.8,5.4,3.2,8.6])
ar2 = arr.array('d',[1.4,3.4,5.6,7.6,9.8,5.4,3.2,8.6])
ar3 = ar1+ar2
print(ar3)'''

'''d = range(10)
f = [0,1,2,3,4,5,7,8,9]

for i in d:
    if i not in f:
        print(i)
'''

'''d = [1,2,3,4,5,6,5,4,3,3,54,56,6,67,56,5,5,4,4,34,3,3,3,3,4,5,56,6,6]
l = len(d)
for i in range(l):
    for j in range(i,l):
        if d[i] >d[j]:
            d[i],d[j] = d[j],d[i]
print(d)'''


'''s = list(input("Enter your numbers: ").split(" ",10))
print(s)'''

'''t = ('hello',3,2,5,6,5,'55','90',6)
t1 = t
print(t)
print(t1)
print(id(t))
print(id(t1))'''

'''t = ['hello',3,2,5,6,5,'55','90','6']
t1 = ['hello',3,2,5,6,5,'55','90','6']
print(t)
print(t1)
print(id(t))
print(id(t1))'''

# Even if they are having same data id's will be different fot mutable data types.
# If they are having same data id's will be same for immutable data types.

'''t = ('hello',3,2,5,6,5,'55','90',6)
t1 = t[1:5]
print(t)
print(t1)
print(id(t))
print(id(t1))

p = [1,2,(3,4,5),6,(7,8,9,10)]
print(p)
u = (1,2,3,[5,6,7])
print(u)'''

'''import numpy as np
t = (1,2,3,4,5,np.nan,False)

print(all(t))

t1 = (True,2,3,4,False)
t2=()
print(any(t2))'''

'''t = ('a','b','c','d','e')
for i,j in enumerate(t):
    print(i,j)'''

'''T1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(T1[-2:-5:-1])'''

'''tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222 # this will work because we can replace the value inside listso
tuple1[0] = 2000 # this won't work we can't replace the value inside tuple
print(tuple1)'''

'''tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
l = list(tuple1)
print(l)
l.sort(key= lambda x: x[-1])
print(l)
'''

'''d={'a':20,'b':59,'c':90}
for i in d:
    print(i)'''

'''sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)'''

'''set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.symmetric_difference(set2)
print(set3)'''

'''d = {101:'al',102:'bl',103:'jhjf'}
f = {104:'grg',105:'kjhgkfgh',106:'torut'}
#print(d.get(101))
#f= d.pop(106,'not found')
d.update(f)
print(d)
t = d.setdefault(105,'this is set')
print(t)
print(d.keys())
print(d.values())
print(d.items())
#print(d.has_key(105))

print(d.get(105,'not found'))

Key=(101,102,103,104)
Value="Geekyshows"
t1 = dict.fromkeys(Key,Value)
print(t1)'''

'''l1 = [i+1 for i in range(20) if i%2 !=0]
print(list(l1))

l1 = [i for i in range(20) if i%2==0]
print(list(l1))

l1 = [ 'T' if i%2==0 else 'F' for i in range(20)]
print(l1)

l2 = ['True' if i%2==0 else 'False' for i in range(20)]
print(l2)

s = {i for i in range(20) if i%2==0}
print((s))
s = { i if i%2==0 else str(i)+' '+'False' for i in range(20)}
print(s)'''

'''d = {i:(i*2 if i%2==0 else 'Zero') for i in range(20)}
print(d)

d1 = {i:(i*2) for i in range(10) if i%2==0}
print(d1)'''

'''l=['hffr','ggtgt','rrtrt','khdfhd','ofueiue']
for i,v in enumerate(l):
    print(i,v)'''

'''q=['a','b','c','d','e']
a = ['Apple','Ball','Cat','Dog','Elephant']

for q1,a1 in zip(q,a):
    print(q1,a1)

r = zip(q,a)
print(list(r))'''

'''l = {'a':1,'b':2,'c':3,'d':4}

for i,v in l.items():
    print(i,v)
'''

'''def student(fname,lname):
    print(fname,lname)

student(fname='Ahammad',lname='Shaik')
student(lname='Ahammad',fname='Shaik')'''

'''def Student(d=20,k):
    print(d,k)
#Student(40,50)
#Student(40)
Student(67,58)'''

'''def Student(*args):
    for i in args:
        print(i)

Student('Ali','Ahammad','Gopi','Nath reddy','Jameer','Saleem','Mastanvali')'''

'''def Student(**kwargs):
    for i,v in kwargs.items():
        print(i,v)
Student(name='Ahammad',age=25,salary=25000,company='Accenture')'''

# Pass a function as parameter to another function

'''def Func1(show1):
    print('hello students this is: '+show1())

def show():
    return 'Ahammad'

Func1(show)'''

'''def Remo():
    def Ram():
        return "Hello Ram"
    #f = Ram()
    return Ram

r = Remo()
print(r())'''

# new object will create
'''def Func1(x):
    x=20
    print(x)
x=30
Func1(x)
print(x)'''

# new object will not be created because list is mutable
'''def Func1(x):
    x.append(100)
    print(x)
x=[34,32,45,67,65,89]
Func1(x)
print(x)'''

'''def Func1(x):
    print(id(x))
    x=[1,2,3,4,5,6,6]
    print(x,id(x))

x=[34,32,45,67,65,89]
print(x,id(x))
Func1(x)
print(x,id(x))'''

'''def myFun(x):
    x[0] = 20
# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)'''

'''import monk

def monkchanged(self):
    print('Changed monk is called')

monk.Monk.showmonk = monkchanged
obj = monk.Monk()
obj.showmonk()'''

'''def fact1(a):
    if a==1:
        return 1
    else:
        return(a*fact1(a-1))
a=5
print(fact1(a))'''

'''a=40
b=50
c = lambda a,b:a+b
print(c(a,b))'''

'''add = lambda x:(lambda y:x+y)
a = add(10)
print(a)
print(a(20))'''
''' 
def show(a):
    print(a(8))
show(lambda x:x+20)

print((lambda x:x+1)(20))
'''

'''def simpleGenerator():
    yield 1
    yield 2
    yield 3

a = simpleGenerator()
print(a)
for i in a:
    print(iter(i))'''

'''keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d={}
for i,v in zip(keys,values):
    d[i]=v
print(d)'''

'''dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)'''

'''sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])
'''

'''employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
d=dict.fromkeys(employees,defaults)
print(d)'''

'''sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

d={}
d['name'] = sample_dict['name']
d['salary'] = sample_dict['salary']
print(d)'''


'''sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

del sample_dict['name']
del sample_dict['salary']
print(sample_dict)
'''

'''sample_dict = {'a': 100, 'b': 200, 'c': 300}
for i in sample_dict.values():
    if i== 200:
        print('The value 200 is present')'''

'''sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}


sample_dict['location'] = sample_dict.pop('city')

print(sample_dict)'''

'''sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

h = min(sample_dict.values())

for k in sample_dict.keys():
    if sample_dict[k] == h:
        print(k)'''

'''sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)'''

'''def sam(x):
    return x.value()
a = {'A':10,'B':1,'C':2,'D':22,'E':0}
t = tuple(a.items())
t1 = sorted(t,key= lambda x: x[-1])
print(t1)
d = dict(t1)
print(d)'''

'''d= {}
for i in range(15):
    d[i] = i*i
print(d)'''

'''d= dict(foo=100,bpo=200)
print(d)
print(type(d))

d1={('foo',12),('boo',67)}
print(d1)
print(type(d1))'''

'''dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)'''

'''dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.pop("age")
print(temp)'''

'''dict1 = {'GFG':1,'Google':2,'GFG':3}
print(dict1)
print(dict1['GFG'])'''

'''d = {'key':0,'key':0}
print(d)

lst = [('key',0),('key',0)]
print(dict(lst))

d = {}
d['key'] = 0
d['key'] = 0
print(d)'''

'''def checkprime(a):
    if a>0:
        c=0
        for i in range(2,a):
            if a%i ==0:
                c +=1
        if c ==0:
            return True
        else:
            return False
    if a==1:
        return True
a=7
s = checkprime(a)
if s== True:
    print('given number is prime')
else:
    print('given number is not prime')'''

'''def show(l):
    if len(l) ==1:
        return l[0]
    else:
        return l[0]+show(l[1:])

L = [1,2,3,4,5,6,7,8,9,10]
print(show(L))'''


'''def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

n=5
print(fact(n))
'''

'''def fact1(n):
    if n==1:
        return n
    else:
        return n*fact1(n-1)
n=10
print(fact1(n))'''

'''def febno(n):
    if n<=1:
        return n
    else:'''


# 0, 1, 1, 2, 3, 5, 8, 13,…

'''def shame(n):
    l=[]

    a,b = 0,1
    l.append(a)
    l.append(b)
    for i in range(2,n):
        c = a + b
        a=b
        b = c
        l.append(b)
    return l
n=10
s = shame(n)
print(list(s))'''

'''def rec(n):
    if n<=1:
        return n
    else:
        return rec(n-1) + rec(n-2)
n=10
s = rec(n)
print(list(s))
'''


'''def poww(base,power):
    if base==1:
        return base
    else:
        return base*(poww(base,power-1))
base=2
power = 4
d = poww(base,power)
print(d)'''

#def func():
#    '''hello this is doc string'''

#func()
#print(func.__doc__)

'''def fun(a):
    d = a()
    return d+" world"

def show():
    return "hello"

s = fun(show)
print(s)'''


'''def fun():
    def show():
        return 'show func'
    print('the called function is!!!')
    return show

s = fun()
print(s())'''


'''def dec1(func):
    def inner():
        print("Executing now!!!")
        func()
        print("Execution ends")

    return inner
@dec1
def who():
    print("I am an intermediate peron in python")

who()'''

'''def pope(s):
    def inner():
        d = s()
        return d.upper()
    return inner

@pope
def show():
    return 'hello there'

print(show())'''

'''s = lambda x=10:(lambda y:x+y)
d = s()
print(d(20))

def simplegen():
    yield 1
    yield 2
    yield 3

for value in simplegen():
    print(value)'''

'''def simpleGenerator():
    yield 1
    yield 2
    yield 3

x = simpleGenerator()

for i in range(3):
    print(x.__next__())'''

'''def my_gen():
    n=1
    print("This is printed first")
    yield n

    n +=1
    print("This is printed second")
    yield n

    n +=1
    print("This is printed last")
    yield n


for i in my_gen():
    print(i)

x = my_gen()

for i in range(3):
    print(x.__next__())'''


'''s='hello geeks this is geeks for geeks'
d = s.__iter__()   # or iter(s)
l = len(s)
print(d.__next__())
for i in range(l):
    print(d.__next__(),end=' ')'''

'''def outerfunc(text):
    text = text
    def innerfunc():
        print(text)
    return innerfunc
f = outerfunc('hello')
f()'''

'''def show(a):
    def inner(r):

        if r%2==0:
            return True
        else:
            return False

    return inner

@show
def sample(e):
    return e
e=33
print(sample(e))'''

'''if __name__ == '__main__':'''

'''class Model1:
    def __init__(self):
        self.name='Ali'
        self.age = 25
    def getinsta(self):
        print(self.name+' '+str(self.age))

d = Model1()
d.getinsta()'''

'''class Meta1:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    def methnum(self,p):
        return self.v1+" "+self.v2+" "+str(p)

m = Meta1('Ahammad','Shaik')
m1 = Meta1('Ahammad1','Shaik1')
k = m.methnum(300)
k1 = m.methnum(3001)
print(k)
print(m.v1)
print(id(m1))
print(id(k1))'''

'''class Monk:
    fp=20
    def __init__(self,a):
        self.a = a
    def mortan(self):
        return self.a

    @classmethod
    def fp_method(cls):
        return cls.fp
d = Monk(200)
print(d.mortan())
print(d.fp_method())
print(Monk.fp)'''

'''class Mobile:
    fp = 'Yes'

realme = Mobile()
redmi = Mobile()
r1 = Mobile()
print(Mobile.fp)
print(realme.fp)
print(redmi.fp)
print(r1.fp)
Mobile.fp = 'No'
print(Mobile.fp)
print(realme.fp)
print(redmi.fp)
print(r1.fp)'''

'''class Mobile:
    fp = 'Yes'

realme = Mobile()
redmi = Mobile()
r1 = Mobile()
print(Mobile.fp)
print(realme.fp)
print(redmi.fp)
print(r1.fp)
realme.fp = 'No'
print(realme.fp)
print(Mobile.fp)
print(redmi.fp)
print(r1.fp)'''


'''class Car:
    def __init__(self,carname):
        self.__make = carname

    def set_make(self,carname):
        self.__make = carname

    def get_make(self):
        return self.__make

mycar = Car('Lambargini')
print(mycar.get_make())
mycar.set_make('BMW')
print(mycar.get_make())'''

'''class Father:
    def show(self):
        print('Father show method')

class Son(Father):
    def show1(self):
        print('Son show method')

f = Father()
f.show()
s = Son()
s.show1()
s.show()'''

'''class Father:
    def __init__(self):
        print('father constructor method!!!')
    def show(self):
        print('This is show method')

class Son(Father):
    def __init__(self):
        super().__init__()
        print('Son constructor method!!!')
    def show1(self):
        print('This is show1 method')

s = Son()
s.show()
s.show1()'''


'''class Father:
    def show(self):
        print('father class method')

class Son(Father):
    def show1(self):
        print('Son class method')
class Grandson(Son):
    def show2(self):
        print('Grand child relation')

g = Grandson()
g.show2()
g.show1()
g.show()'''

'''from abc import ABC,abstractmethod
class Polygon(ABC):
    def show1(self):
        print('show1')

    @abstractmethod
    def show2(self):
        pass

    @abstractmethod
    def show3(self):
        pass

class Pentagon(Polygon):
    def show2(self):
        print('this method is show2')

    def show3(self):
        print('this method is show3')

p = Pentagon()
p.show1()
p.show2()
p.show3()'''

'''with open('demo.txt','r') as p:
    print(p.read())'''

'''f= open('demo.txt',mode='w')
f.write('who are you')
f= open('demo.txt',mode='r')
print(f.read())'''

'''f = open('student5.txt', mode='r', encoding = 'utf-8')
d = f.read()

#m= f.readlines()
for i in d:
    print(i)'''

# Regular Expressions
'''import re
s='GeeksforGeeks: A computer science portal for geeks'
match = re.search(r'computer',s)
print("Start index: ",match.start())
print("End index: ",match.end())'''

import re
'''s="geeks.forgeeks"
match = re.search(r'.',s)
print(match)

match1 = re.search(r'\.',s)
print(match1)'''

'''s="geeky shows"
match = re.search(r'^geeky',s)
print(match.start())'''

'''string="""Hello my Number is 123456789 and
            my friend's number is 987654321"""

regex = r'\d+'

start = re.findall(regex,string)
print(start)'''

'''r = re.compile('[a-e]')
print(r.findall("Aye, said Mr. Gibenson Stark"))'''

'''p = re.compile('\d+')
f = p.findall("I went to him at 11 A.M. on 4th July 1886")
print(f)'''

'''p = re.compile('\w')
print(p.findall("He said * in some_lang."))

p = re.compile('\W')
print(p.findall("I went to school at 11 A.M., he \
said *** in some_language."))

p = re.compile('\w+')
print(p.findall("I went to school at 11 A.M., he \
said *** in some_language."))

p1 = re.compile('\W')
print(p1.findall("he said *** in some_language."))'''


'''f = re.compile('ab*')
print(f.findall("ababbaabbb"))'''

#from re import split
'''import re
print(re.split('\W+','Words, words , Words'))
print(re.split('\W+',"Word's words Words",2))
print(re.split('\W+','On 12th Jan 2016, at 11:02 AM'))
print(re.split('\d+','On 12th Jan 2016, at 11:02 AM'))
print(re.split('\d+','On 12th Jan 2016, at 11:02 AM',1))
print(re.split('[a-f]','Aey, Boy oh boy, come here'))
print(re.split('[a-f]+','Aey, Boy oh boy, come here',flags=re.IGNORECASE))'''

#import re

'''p = re.sub(r'ub','@#','Subject has Uber booked already',count=1,flags=re.IGNORECASE)
print(p)'''

'''print(re.subn('ub','@#','Subject has Uber booked already',flags=re.IGNORECASE))'''

'''print(re.escape("This is Awesome even 1 AM"))'''

'''regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex,"I was born on June 24")
if match != 'None':

    print('Starting index {0} and ending index {1}'.format(match.start(),match.end()))
    print('Full Match %s'%(match.group(0)))
    print('Month: %s'%(match.group(1)))
    print('Date: %s'%(match.group(2)))'''

'''import re
s="Welcome to GeeksForGeeks"
res = re.search(r'\bG',s)
print(res.re)
print(res.string)
print(res.start())
print(res.end())
print(res.span())'''

'''import re
s="Welcome to GeeksForGeeks"
res = re.search(r"\bGea",s)
print(res.start())
print(res.end())
print(res.span())'''

import re
'''s="Welcome to GeeksForGeeks"
res = re.search(r"\D{2} t",s)
print(res.group())'''

'''regex_email = re.compile(r'^([a-z0-9_\.-]+)@([a-z0-9\.-]+)\.([a-z\.]{2,6})$',re.IGNORECASE)

# Using verbose name
regex_email = re.compile(r"""
^([a-z0-9_\.-]+)   # local part
@   # single @ sign
([0-9a-z\.-]+) # Domain name
\.  # Single dot
([a-z]{2,6})$  # Top level domain

""",re.VERBOSE|re.IGNORECASE)'''

'''def validate_email(email):
    regex_email = re.compile(r"""
    ^([a-z0-9_\.-]+)    # Local part
    @     # Single sign
    ([0-9a-z_\.-]+)   # Domain name
    \.     # single dot
    ([a-z]{2,6})$     # Top level domain
       
    """,re.VERBOSE|re.IGNORECASE)

    res = regex_email.fullmatch(email)

    if res:
        print("{} is valid: Details as follows".format(email))
        print("Local: {} ".format(res.group(1)))
        print("Domain: {} ".format(res.group(2)))
        print("Top level domain: {}".format(res.group(3)))
        print()

    else:
        print("{} is Invalid".format(email))

validate_email("expectopatronum@gmail.com")
validate_email("avadakedavra@yahoo.com@")
validate_email("Crucio@.com")'''


'''def password_check(passwd):
    Special_Symbol = ['$','!','@','%','^','&','*']
    val = True

    if len(passwd) >6:
        val = True
    if len(passwd) <21:
        val = True
    if not any(i for i in passwd if i.isdigit() == True):
        val = False
    if not any(i for i in passwd if i.isupper() == True):
        val = False
    if not any(i for i in passwd if i.islower() == True):
        val = False
    if not any(i for i in passwd if i in Special_Symbol):
        val = False

    if val:
        return True
    else:
        return False

t = password_check('asd123')
if t == True:
    print('Password is valid')
else:
    print('Password is invalid')'''


'''import re
pattern = "^.*(?=.{8,20})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&+=]).*$"
password = input("Enter password: ")
result = re.findall(pattern,password)
if result:
    print("Password is valid")
else:
    print("Password is not valid")
'''


'''import re
reg = re.compile('[8 9]\d{9}')
f = reg.findall('9666666660')
if f:
    print("Phone number is valid")
else:
    print("Phone number is not valid")'''

'''import re
reg = re.compile('[A-Z][a-z][0-9]{1}')'''

import re
from getpass import getpass
passwd = getpass("Enter the password: ")
print(passwd)















