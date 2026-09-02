#Day 10 -- Mapping DataType --> Dictionary

#Dictionary --> Collection of key-vlue pairs
#it is Mutable,Ordered
#it is denoted using flower Braces {} or dict() method.
#in dictionary we index by using the keys
'''
details = {}
print(details)
print(type(details))

#it is structured as Key:Value

details = {'Name':'Pavan','Place':'Hyd','age':23}
print(details)
print(len(details))

#Accessing values in Dictionary
#to access a value in dictionary we require its key

print(details['Name'])
print(details['Age']) #raises an error because the key Age does not exist
#keys in a dictionary must be unique,
#if keys are duplicated in the dictionary, only the last occurance is considered.

data = {'Age':25,'name':'code','Age':26}
print(data)
'''

students_data = {'Ids':[21,23,52,27],
                 'Name':['pavan','abhiram','nihanth','sathwik'],
                 'Place':('hyd','vij'),
                 'Gender':{'male','female'}}
'''
print(len(students_data))
print(students_data.keys()) #key() method returns the keys in the dictionary
print(students_data['Name'])

print(students_data.values())#values() method returns the values in the dictionary

students_data['Course'] = ['PFS','JFS','DA','AAA']
#print(type(students_data))
#print(type(students_data['Ids']))

students_data['Ids'].extend([56,67,87]) #when updating a list use the method not the = operator
#print(students_data)

#we want to insert a new value in the place key
students_data['Place'] = list(students_data['Place'])
#print(students_data['Place'])

#we want to append viz to the list of places
students_data['Place'].append('viz')
#print(students_data['Place'])

print(students_data['Course'][1:3]) #prints jfs and da
del students_data['Ids'][1:3]
print(students_data['Ids'])
#we dont have list methods to delete multiple values together, so only way is to use the del keyword

students_data['Name'].sort()
print(students_data['Name']) #sorts the values in the name key in alphabetical orde
r
#Dictionary method --> keys(),values(),items()
print(students_data.items()) #returns key-value pairs as tuples

#get() method returns value is key exists in the dictionary else returns None
print(students_data.get('Branch')) #returns None
#print(students_data['Branch']) #raises a key error

#setdefault() method
#if the key is present then returns the values else creates a new key with the mentioned key
students_data.setdefault('branch',[1,2,3,4])
print(students_data)

#update()
#update() method can be used to update a dictionary but must be updated using another dictionary
'''
students_data.update({'fees':[455,234],'marks':[57,73,53]})
#print(students_data)

#pop() method
# removes the specified element and returns the values of the key
#print(students_data.pop('marks'))

#popitem() method
#removes the last element from the dictionary and returns the values of the specified key
#returns the key-value pair as a tuple
students_data.popitem()
#print(students_data)

#fromkeys() method
#only to make a new dictionary from a iterable variable like list or set or tuple
#but it only sets the values to None, we have to modify the values later
d = dict.fromkeys(students_data['Name'])
#print(d)

#membership operator on dictionary
#print('nihanth' in d) #returns true if the mentioned key is present else false

#nested dictionaries









































