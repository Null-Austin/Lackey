# Libaries
import os
import json
import re

# local functions
def path(path):
    return os.path.join(os.path.dirname(__file__), path)    

# get tokens
data = open(path('data/tokens.txt'),'r', encoding='utf-8')
data.readline()  # skip the first line with token count
tokens = json.loads(data.readline())
data.close()

# usable functions
def encode_tokens(s):
    s = str.lower(s) 
    indices = []
    words = s.split()
    words = [re.sub(r"[^a-zA-Z0-9]", "", word) for word in words]
    for word in words:
        if word in tokens:
            index = tokens.index(word)
            indices.append(index)
    return indices

def decode_tokens(token_indices):
    words = []
    for token in token_indices:
        token = int(token)
        words.append(tokens[token])
    return ' '.join(words)