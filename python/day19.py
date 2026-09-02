#Day 19 --> Pass by value and Pass by Object Reference, Built in functions

#Pass by value
#Pass by object reference

#pass by value reference --> Immutable Objects (int,float,str,tuple,frozenset)
'''
def update(number):
    """Pass by value Reference works"""
    number *= 5
    return number
print(update(5))
number = 23
print(update(number))
print(number)
'''
'''
def lst_work(lst):
    """checking pass by reference """
    lst.pop()
    return lst

lst = [1,2,3]
print(lst_work(lst))
print(lst)
'''

#functions are termed as first class objects --> 
#a function inside antoher function
#a function can be used as a argument to antoher function -> list(map(input()))
#a function can call itself (recursive functions)
#a function can return another function

#Built-in functions --> Python by default has build-ins which makes the logic easier

#print(len(dir(__builtins__))) #155
#abs function
#print(abs(-1.15))
'''
#all function
data = [None]
#print(all(data))

#any function
print(any(data))

#binary function
print(bin(6)) #returns the binary value of a character
print(chr(32)) #returns the character associalted with the given ascii value
print(bool(0)) #converts into boolean value
print(complex()) #converts a number into complex value
print(dict(name = 'pavan',place='hyd')) #converts the given arguments into dictionary
'''
''' 
print(divmod(5,3)) #returns the division modulus in a tuple
print(enumerate() #creates a counter variable
'''
details = ['codegnan','pavan','AAI']
dictionary = dict(enumerate(details))
for i in range(len(details)):
    print(i,":",details[i])

