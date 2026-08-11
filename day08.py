#day 8 - sets and frozensets

#tuples --> Sequence Datatype
#tuples are an immutable, ordered,indexed sequence type
#we use () brackets to declare a tuple
'''
#initialization of tuple
data = 2,3,4 #when we give a sequence of values without any brackets, it automatically becomes a tuple
#a tuple can also store heterogeneous data like list
print(data)
print(type(data))
'''
#nested tuples and also have lists inside it
#details = ('codegnan',32,(2,4,5),'saketh',[12,45,'agents','rag'])
'''print(details)
print(len(details)) #it returns tuple as output
print(details[4][2])

#my output should be as below
#('codegfaf',32,(2,4,5),'saketh',[12,45,'agents','rag'])
print(details)

print(details[0])
details[0] = details[0].replace('n','f') #because tuples are immutable we cant modify it
print(details)

details[4][2] = details[4][2].replace('A','a') #we can modify the list inside the tuple.
print(details)
print(details[1:4])

print(details[::3])
details[4].remove('agents')
print(details)

#operations on tuples.
#indexing,slicing,membership,concatenation,repetition,merging

age = 21,22,32,25
ids = 231,342,213
print(age + ids) #merging
print(age * 3)
print(231 in ids) #membership

#methods on tuples
#len(),type(),min(),max()

age = (25,12,45,65)
print(min(age))
print(max(age))
print(tuple(sorted(age))) #sorted gives a list so we convert it into tuple using type conversion
list(age).reverse()
print(age)

#index(), count()
details = ('saketh','codegnan','agentic ai',34,23,5.8)
print(details)

print(details.index(34))
print(details.count(34))

#tuple --> list (typecasting)
details = list(details)
print(details)
print(details)
print(type(details))

#convert string to list/tuple

s = 'string'
print(list(s))

#set datatype --> sets and frozen sets
#sets --> set is a unique,mutable and unordered collection
#we use set() to denote a set
#a set does not have index like list and tuple
a = {} #this by default will be a dictionary not a set
b = set()

print(type(a))
print(type(b))

ids = {123,124,125,126,127,123,124} #a set eliminates duplicate values and only stores unique values
print(ids)
print(len(ids))

#as set is mutable, we can insert and remove elements
#a set cannot have another set inside it
#a set cannot have list inside it
#but a list can have a tuple inside it.
data = {23,4.5,'codegnan',(12,34,12)} #a tuple that can store repeting values can still be stored in set
print(data)

ids = {123,124,125,126,127,123,124}
print(ids)
#add(),update()

ids.add(156)
print(ids)
ids.add("AAI")
print(ids)

ids = {123,124,125,126,127,123,124}
ids.update([12,23])
print(ids)

#remove elements from a set --> discard(),remove(),clear()
ids = {123,124,125,126,127,123,124}
ids.discard(123)
print(ids)
ids.remove(124)
print(ids)

#ids.remove(123) #remove returns a key error when a value is not present in the list
#ids.discard(123) #discard avoids error when a the value is not present in the list

ids.pop() #removes a random element from the list
#pop() raises an error when the set is empty
#clear() removes all the values from the set, when nothing to return it gives None
'''

#union,intersection,difference,symmetric difference,subsets,supersets
ids = {123,124,125,126,127}
#age = {35,23,123,24,45}
'''
c = ids.union(age)
print(c) #returns the uncommon values from the two sets
e = ids.update(age)
print(ids) #returns the uncommon values from the two sets but the result is now in ids not in e unlike union()method

d = ids.intersection(age)
#print(d) #returns the common element in both the sets
f = ids.intersection_update(age) #works like update function but intersects the values into id
print(ids)

#h = ids.difference(age)
#print(h) #removes the common elements and returns the uncommon elements from first set

# |(union) , &(intersection), -(difference), ^(symmetric difference)
#g = age - ids
#print(g)

#a = age ^ ids
print(a) #removes the common elements from both the sets and returns the uncommon elements from both the sets

a = {1,2,3}
b = {1,2,3,4,5}

print(a.issubset(b)) #returns true if a is a part of b, else returns false
print(b.issuperset(a)) #returns true if b has elements of a in it, else returns false

print(a.isdisjoint(b)) #returns true if no element of first set is present in second set, else returns false
'''

#Frozenset() --> immutable set, ordered
data = frozenset(ids)
print(data)
print(type(data))

#a frozenset cannot be modified but mathematical operations can be performed on them
temp_details = frozenset([34,35,34,32,31])
print(temp_details)
print(min(temp_details))
print(max(temp_details))
print(sorted(temp_details))


#make a nested sequence 










































