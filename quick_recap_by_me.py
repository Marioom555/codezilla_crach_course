
# First program 
print(" Helloo Every body , iam Maryoom ^-^")
print("    / |")
print("   /  |")
print("  /   |")
print(" /--- |")


# ----------------------------
# Nubers & some functions
y= 10.5
print(str(y))
print(abs(y))
print(pow(y,2))
print(max(y,4))
print(min(y,4))
print(round(y))
from math import * 
print(ceil(2.1))
print(floor(2.1))
print(sqrt(9))

# --------------------------
# Getting inputs
name = input("Enter your name : ")
age = input("Enter your age : ")
print("Hello "+name+ " your age is "+age)

# -------------------------
# Building A Calculator
num1=float(input("Enter the first no.:"))
num2=float(input("Enter the second no.:"))

print(num1*num2)
print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1%num2)


# ------------------------
# MadLips Game 
color= input(" Enter a color : ")
plural_name= input(" Enter a plural name : ")
adjective= input(" Enter an adjective : ")

print(f"trees are {color}")
print(f" {plural_name} are mean")
print(f"please keep it {adjective}")


# ---------------------------
# Lists 
l=[1,'Memo','akouna','programming']
print(l[1])
print(l[1:3])
print(l-[2])
l[1]='sos'
print(l[1])
l1 = [1, 'Memo', 'akouna', 'programming']
l2 = [15, 'Mamista', 'koty', 'bro', 6]
l2.extend(l1)
print(l2)
l1 +=l2
print(l1)
l1.append('ashraf')
l1.append([1,'ashraf'])
l1.insert(0,'iron woman')
print(l1)
print(l2.remove(15))
l2.clear()
l1.pop()
what_was_popped=l1.pop()
print(l1.index(1))
print(l1.count(1))
l1.append(1)
print(l1.count(1))
l1=l2
l1.append(1)
print(l1)
l1.copy()  #shallow copy
l1.append(5)
print(l1)

# -------------------
# Tuples
cordinates=(25,80)
list_of_tuples=[(1,2),(34,78),(90,56)]
print(cordinates[0])
print(cordinates[1])
print(list_of_tuples[0])
print(list_of_tuples[0][0])

# -----------------------
# Functions

def say_hi(name):
    print(f"Hello {name} ^_^ ")
name=input("Enter your name : ")
say_hi(name)

def cub(num):
    return num*num*num
    print("hello")   # it will not printnted because the return function ends the function running 
print(cub(3))

# ----------------------------
# python conditions

is_hungry = True
wants_to_eat=False
if is_hungry and wants_to_eat:
    print(" Goo eat dude ~ ")
elif is_hungry and not wants_to_eat:
    print("eat so you can survive bro ")
else:
    print(" Don't eat ")

# -----------------------------
# comparisons
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=3 :
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(4,7,8))
print(max(9,8,0))

# ---------------------------
# Build Calcualator
num1= float(input("Please Enter the first number : "))
operator= input("please Enter the operator: ")
num2= float(input("Please Enter the second number : "))

if operator == '+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    print(num1/num2)
else:
    print("you enter wrong operator ")


# ------------------------------
# Dictionaries

convert_month={
    "jan":"january",
    "feb":2,
    3:"march",
}
print(convert_month[3])
print(convert_month.get('feb'))
print(convert_month.get('mom',"this value dosn't exist" ))

# ---------------------------------
# while loops
i = 1
while i <= 10:
    print(i)
    if i == 5:
        i += 1
        continue      
    if i == 8:
        break       
    i += 1
else:
    print("the condition is not true")
print("the loop has ended >_<")

# ------------------------
# for loops 
for char in "Marioomaa":
    print(char)

l=[1,2,3,5]
for num in l:
    print(num)

for num in range(len(l)):
    print(l[num])

for i in range(8):
    print(i)

for i in range(2,18):
    print(i)

for i in range(len(l)):
    if l[i] == 3:
        print("You find me ^_^ ")
        print(f"i was in place {i} >_< ")
        break

# ---------------------------
#Sets
# first solution
l1=[1,2,4,8,9,6,3,5,3,5,73,35,26,64,76,5,6,3,5,636,336,5]
l2=[]
for number in l1:
    if number not in l2:
     l2.append(number)
print(l2)


# second solution
unique_set=set(l1)
print(type(unique_set))
print(dir(unique_set))  # print all methods works with sets

# ------------------------------------
# Exponent function 
def power (base,pow):
    res=1
    for index in range (pow):
         res= res * base
    return res
print(power(2,2))

# ---------------------------------------
# 2D list & insted loops
no_list= [
    [1,2,3],
    [5,7,8],
    [8,8,0]
]
print(no_list[1]) 
print(no_list[1][1])
for row in no_list:
    for col in row:
       print(col)

# ------------------------------------------
# Python Errors 
try:
    result = int(input("Enter your input: "))
    print(result)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)

# ----------------------------------------
# Reading Files 
names=open("names.txt",'r') # read mode 
# open("names.txt",'r+') # read&write mode 
# open("names.txt",'w') #  write mode
# open("names.txt",'a') # append mode 

# print(names.readable()) # boolean value
# print(names.read()) # print all file
# print(names.readline()) # print one line 
# print(names.readlines()) # print all lines and put them in list
# print(names.readlines()[3])
for name in names:
    print(name+ " is cool " )
names.close()

# -----------------------------
# Writing Files 
names=open("names.txt",'a') # write mode 
names.write("\n hunter ")
names.close()

names=open("characters.txt",'w') # write mode 
l=['\nmariam','\n Ashraf','\n rivo']
names.writelines(l)
names.close()

names=open("index.html",'w') # write mode 
names.write("<p>AKOUNA MATA <\p> ")
names.close()

#------------------------------
# Modules
import useful_fun
print(useful_fun.coll_dice(9))

# -----------------------------
# objects & classes

from employee import Employee
employee1 = Employee("islam", 50, "Codezilla", True,9,2000)
employee2 = Employee("ibrahim", 60, "Facebook", False,7,1000)
print(employee1.name)
print(employee1.age, employee2.age, employee2.department, employee1.is_manager)
print(employee1.is_excellent)
print(employee2.is_excellent)
print(employee1.salary)
employee1.bonus()
print(employee2.salary)
employee2.bonus()

from doctor import Doctor
from doctor import FamilyDoctor
doctor1 = Doctor()
doctor1.studied_years()
doctor1.works_where()
doctor1.paid_by_who()

doctor2=FamilyDoctor()
doctor2.what_specialization()

# --------------------------------------
# 1- What do args* and **kwargs mean?
# 2- How to use them and why?
# 3- How to unpack iterables with * and **?

def sum_nums(*args):   # arguments here like tuple
    result = 0
    for x in args:
     result += x
    return result

def my_sum(a, b, *args, option=True):
    result = 0
    if option:
     for x in args:
      result += x
     return a + b + result
    else:
     return result

def make_sentence(**kwargs):  # arguments here like dictionary 
    result = ""
    for x in kwargs.values():
     result += x
    return result

def print_args(x, y, *args, option=True, **kwargs):
    print(x, y)
    print(args)
    print(option)
    print(kwargs)
print_args(1, 2, "3 is args", "4 is args", "5 is also args", option=False, channel="codezilla")

my_first_dict = {"A":1, "B":2}
my_second_dict = {"C":3, "D":4}
my_merged_dict ={**my_first_dict, **my_second_dict}
print(my_merged_dict)
list_of_char = [*"codezilla","Maryam" ]

print(list_of_char)