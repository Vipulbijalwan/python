"""
1- reusability
2- modularity
3- scoping
"""

def greet():
    print("hii")
greet()

## passing parameter

def greet2(str):
    print(f"hii",str)
greet2("vipul")# argument

# default values

def greet3(name='vipul',city='DDUN'):
    print(f'Welcome {name} to the {city}')


# greet3() output- Welcome vipul to the DDUN
greet3('vikas','Delhi') #output- Welcome vikas to the Delhi


