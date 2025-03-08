"""
1- ordered
2- mutable
3- indexed
4- duplicate values
5- heterogenous
6- dynamic
"""


my_list2=[23,45,67,89,56,77]
my_list=[1,2,"hello",3.5,True]
print(my_list)

my_list[0]=100 # update value of list
print(my_list)

my_list[0:3]=[100,200,300] # update multi value 
print(my_list)

print(my_list+my_list2)# concatination

print('hello' in my_list)# check value in list

""""
list 1=[1,2,34,4]
list 2=list1

list 2[0]=100

it can also change the value of list 1

list 1=[1,2,34,4]
list 2=list1.copy()

list 2[0]=100

it can not change the value of list 1
"""

list1=[1,2,34,4]
list2=list1.copy()

list2[0]=100

print(list1,list2)

list1.append(10000)# add vale at end 
print(list1)

list1.insert(2,2000)# add value at specific position
print(list1)

list1.remove(2000)# remove value
print(list1)

list1.pop(4)# remove value at index based
print(list1)

list2.clear()# clear all values
print(list2)


list1.sort()
print(list1)# sort list

list1.reverse()# reverse list
print(list1)

a=min(list1)# min val
b=max(list1)# max val
print(a,b)

"""
range function

number=range(100)

"""
number=list(range(1,10,1))
print(number)# creating list using range function


"""
list comprehension
[expression for item in list if condition]

e=x**2
item=1 to 10
iterable=1 to 10
condition =even num
"""

squares=[]
for i in range(1,11):
    squares.append(i**2)

print(squares)

squares=[i**2 for i in range(1,11) if i%2==0]
print(squares)