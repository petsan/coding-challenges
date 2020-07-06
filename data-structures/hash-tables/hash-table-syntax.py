# hash tables are closely tied to dictionaries, so we start by defining a dictionary
d = {}

d['key'] = 'value1'
print(d['key']) # value1

del d['key']
# print(d['key']) # KeyError: 'key' # commented out to make the rest of the script run

d['key'] = 'value2'

if 'key' in d:
    print(d['key']) # value2
    
else: 
    print("key does not exist") # key does not exist

del d['key'] # setup for failure case

if 'key' in d:
    print(d['key']) # //command is not reached
    
else: 
    print("key does not exist") # key does not exist
