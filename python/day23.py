#Day 23 --> JSON Module
#to convert python objects to json format and viceversa
#dumps() and loads()

import json
'''
data =  {'Name':"Codegnan","age":7}
print(type(data))
parsed_data = json.dumps(data)
print(len(parsed_data))
print(type(parsed_data))

result = json.loads(parsed_data)
print(type(result))
print(len(result))

print(dir(json))
'''
#counter functions from collections module
'''
from collections import Counter

data = ['A','B','C','A','A','C']
r = dict(Counter(data))
print(r)
'''