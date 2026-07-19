"""
Java Script Object Notation
"""

book = {}
book['jay'] = {
    'name': 'jay',
    'address': 'sector 4, near lack city mall, udaipur',
    'phone': 9898989989
}
book['Kranish'] = {
    'name': 'Kranish',
    'address': 'sector 2, near C21 mall, Indore',
    'phone': 9898989989
}
book['Ajay'] = {
    'name': 'Ajay',
    'address': 'near Robot Circle, Indore',
    'phone': 9898989989
}

import json
s = json.dumps(book)
with open("/home/monkeydluffy/Documents/Books/data.json","w") as f:
    f.write(s)


f=open("/home/monkeydluffy/Documents/Books/data.json","r")

s = f.read()

print(s)

import json
book = json.loads(s)

print(book)


import json

f=open("/home/monkeydluffy/Documents/Books/Funny.txt","w")
f.write("I Love C++")
f.close()

f=open("/home/monkeydluffy/Documents/Books/Funny_02.txt","r")
f_out = open("/home/monkeydluffy/Documents/Books/Funny_wc.txt","w")
for line in f:
    tokes = line.split(' ')
    f_out.write("wordcount:"+str(len(tokens))+lines)

f.close()
f_out.close()












