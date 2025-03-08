"""
python dictionary

value={key:value}
1- key-value pair
2- mutable
3- unordered
4- key should be immutable
5- dynamic
"""

my_dic={
    "Name":'python','version':3.4
    }
print(my_dic)

del my_dic['version'] # deleting value
print(my_dic)

#Methods

profile={
    'name':'raju',
    'age':25,
    'salary':50000
}

age=profile.get('age')#get key
print(age)

keys=profile.keys()# get all keys
print(keys)

#all items

items=profile.items()
print(list(items))

#pop
poped=profile.pop('age')
print(poped)