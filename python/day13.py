#Day 13 -- eval() method,Type conversions and loops
#every build-in data type is a built-in function
#list to dictionary
'''
age = [23,21,43]

d = dict.fromkeys((age),None) #using fromkeys method
print(d)

keys = ["A","B","C"]
values = ["a","b","c"]

d = dict(zip(keys,values)) #using zip method
print(d)

list_pairs = [('a', 1), ('b', 2), ('c', 3)]
d = dict(list_pairs) #if the data is present in list of pairs
print(d)

#str to list,tuple,dictionary

name = 'pavan'
g = list(name)
h = name.split()
i = name.split(',')
print(g,h,i)

#input formatting --> list input,tuple input
#list as input
#eval()

data = eval(input("Enter the list:"))
print(data)
print(type(data))
'''

#Repitition statements(loops) --> for and while
#loops will automate the tasks

'''
for loop is used to iterate the items in a collection (str,list,tuple...) also can generate a swquence of numbers (range)

syntax for:

for <loop_var> in collections/range_function:
    statements to repeat
'''
#marks = [24,25,21,20]
'''
for mark in marks:
    print(mark,end = "\t")

marks = eval('marks = input("Enter marks:")')
total = 0 ; average = 0
for mark in marks:
    total += mark
average = total / len(marks)
print(total)
print(average)

data = [1,3,4.5,'codegnan',3,'agents',2.4]
total = 0
for _ in data:
    if type(_) == int or type(_) == float:
        total += float(_)
print(total)

details = {'names':['sai','Abhi','Ram'],
           'marks':[24,20,28]}

for key,value in details.items():
    print(key,":",value)

#range() method
#range(start,stop,step) --> generates a sequence of values
#range(end) by default start is 0

for i in range(10,-1,-2):
    print(i,end = " ")

#Home task is print below patterns
#A B C D E F G H
#h f d b
'''

#daily workout log --> fitness streak
workout_log = [1,1,1,0,1,1,0]
#longest streak
longest = 0
current = 0

for i in workout_log:
    if i == 1:
        current += 1
    elif i == 0:
        longest = max(longest,current)
        current = 0
longest = max(longest,current)
print(longest)

    





























