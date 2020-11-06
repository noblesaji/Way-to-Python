#!/usr/bin/env python
# coding: utf-8

# #### Question 1

# In[2]:


SkillSanta_Dict = {
    "name":"Sachin",
    "age":22,
    "salary":60000,
    "city":"New Delhi"
}


# In[3]:


SkillSanta_Dict["location"] = SkillSanta_Dict.pop("city")


# In[4]:


SkillSanta_Dict


# #### Question 2

# In[5]:


Original_List = [11, 45, 8, 11, 23, 45, 23, 45, 89]
list_count = dict()
for x in Original_List:
    if x in list_count:
        list_count[x] += 1
    else:
        list_count[x] = 1
print("Printing count of each item ", list_count)


# #### Question 3

# In[6]:


sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
Unique_sampleList = list(set(sampleList))
print("unique items" ,Unique_sampleList)
tuple_sampleList = tuple(Unique_sampleList)
print("tuple", tuple_sampleList)
print("min:", min(tuple_sampleList))
print("max:", max(tuple_sampleList))


# #### Question 4

# In[7]:


def showEmployee(emp_name, emp_salary=50000):
    print("Employee", emp_name, "salary is:", emp_salary)
showEmployee("Eddy", 50000)
showEmployee("Eddy")


# #### Question 5

# In[8]:


def addition(a, b):
    def sum(a, b):
        return a+b
    sum = sum(a, b)
    return sum + 5
addition(5, 6)


# #### Question 6

# In[9]:


def Fibonacci(n):
        if n <= 1:
            return n
        else:
            return Fibonacci(n-1) + Fibonacci(n-2)
n = int(input("Type a positive number: ",))
for i in range(n):
    print(Fibonacci(i))
        
Fibonacci(9)


# #### Question 7

# In[10]:


def displayStudent(name, age):
    print("Name is ", name, "and age is", age)
displayStudent("David", 16)
showStudent = displayStudent
showStudent("David", 16)


# #### Question 8

# In[12]:


def Mobile_Number():
    mob = input("Enter Mobile Number")
    if (len(mob) == 10) and (mob.isdigit()):
        print("Proper Mobile Number")
    else:
        print("Improper Mobile Number")
        Mobile_Number()
Mobile_Number()


# #### Question 9

# In[15]:


def ncapitals():
    str = input("Enter the string: ")
    count = {"UPPER_CASE" : 0, "LOWER_CASE" : 0}
    for case in str:
        if case.islower():
            count["LOWER_CASE"] += 1
        elif case.isupper():
            count["UPPER_CASE"] += 1
        else:
            pass
    print("Original String: ", str)
    print("No. of Uppercase characters: ", count["UPPER_CASE"])
    print("No. of Lowercase characters: ", count["LOWER_CASE"])
ncapitals()


# #### Question 10

# In[26]:


def number(n):
    sum = 0
    for i in range(1,n):
        if n%i ==0:
            sum += i
            return sum
n = int(input("Enter number :"))
print(number(n))
if n == number(n):
    print("It is a Perfect number")
else :
    print("It is not a perfect number")

