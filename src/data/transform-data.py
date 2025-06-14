# libaries
import json
import os
import re

# global scope variables
script_dir = os.path.dirname(__file__)

# data handling
def return_data(file):
    data = file.read()
    file.close()
    data = str.lower(data)
    return data
data1 = return_data(open(os.path.join(script_dir,'english10k.txt'), 'r', encoding='utf-8'))
data2 = return_data(open(os.path.join(script_dir,'englishdict.txt'), 'r', encoding='utf-8'))

data = f"{data1}\n{data2}"
data = data.splitlines()
data = list(set(data))
data = [re.sub(r"[^a-zA-Z0-9]", "", line) for line in data]

# transform data
list = []
for line in data:
    list.append(line.strip())
list = json.dumps(list)
list = f"### token count = {len(data)}\n{list}"

# save transformed data
newData = open(os.path.join(script_dir,'tokens.txt'),'w',encoding='utf-8')
newData.write(list)
newData.close()
print("Data transformed and saved to tokens.txt")