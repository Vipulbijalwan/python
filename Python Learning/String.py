text="hello everyone welcome to python programming"

text2="how are you"
print(len(text)) # length of string

print(text[0]) # print first char of string

print(text[-1]) # print last char of string

print(text[0:10]) # slicing of string

print(text[0:10:2]) # slicing of string with step of 2 even values of string

print(text[::-1] ) # reverse of string

for i in text:
    print(i) # printing all char

print(text.upper()) # convert str to upper case

print(text.lower())

print(text.title()) # covert first char of string to upper char

print(text.capitalize()) # convert first char of str to upper char

print(text*2) # repate str 2 times

print(text+text2) # concatination of 2 str

print(text.find("everyone")) # finding in string

print(text.replace("everyone","all")) # replace char in string

print(text.split(",")) # split string

