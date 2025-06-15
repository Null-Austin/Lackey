import time
import os
import ast
import json
from pprint import pprint

runtime = time.time_ns()
print(f"started: {runtime}")

def path(path):
    return os.path.join(os.path.dirname(__file__), path)

print(3)
conversations = open(path('./movie/movie_conversations.tsv'),'r', encoding='utf-8').read().lower().split('\n')
conversations = [line.split('	') for line in conversations if line]
conversations = [line[3] for line in conversations if line]
conversations = [line.replace('\' \'','\',\'') for line in conversations if line]
conversations = [ast.literal_eval(line) for line in conversations if line]

print(4)
newlines = []
for i in conversations:
    line1 = i[0]
    line2 = i[1]
    
    if line1 and line2:
        newlines.append([line1,line2])

print(5)
ids = open(path('./movie/movie_lines.tsv')).read().lower()
ids = ids.replace('\'','').replace('"','').replace(',','')
ids = ids.split('\n')
ids = [id.split('	') for id in ids if id]

print(6)
def search(id):
    id = id.lower()
    index = next((i for i, sublist in enumerate(ids) if sublist[0] == id), -1)
    return index
    
while True:
    x = input('input: ')
    s = search(x)
    print(s)
    print(ids[s])

print(7)
newlines2 = []
max = len(newlines)
newlines = newlines[:100]
for line in newlines:
    index = newlines.index(line)
    lines = []
    for i in range(2):
        line2 = line[i]
        line2 = search(line2)
        line2 = ids[line2][4]
        lines.append(line2)
    if lines:
        newlines2.append(lines)
    print(f"Line {index}/{max} processed.")
pprint(newlines2)
newlist3 = []
for line in newlines2:
    for i in line:
        newlist3.append(i)
data = open(path('./data.txt'),'w', encoding='utf-8')
data.write('\n'.join(newlist3))
data.close()
print(f"time: {(time.time_ns() - runtime)/1000/1000/1000}")