# Libaries
import os
import json
import re

# local functions
def path(path):
    return os.path.join(os.path.dirname(__file__), path)    

# get tokens
data = open(path('data/tokens.txt'),'r', encoding='utf-8')
l1 = data.readline()
tokens = json.loads(data.readline())

# usable functions
def encode_tokens(s,max_length=False):
    s = str.lower(s) 
    indices = []
    words = s.split()
    words = [re.sub(r"[^a-zA-Z0-9]", "", word) for word in words]
    for word in words:
        if word in tokens:
            index = tokens.index(word)
            indices.append(index)
    if max_length: # this enables the tokenizer to be used for padding, and therfor the ai. max_length is the maxium length that the seq can be a setnence.
        if len(indices)>=max_length or indices[0] == 0:
            return False
        while len(indices) < max_length:
            indices.append(0)
    return indices

def decode_tokens(token_indices):
    words = []
    for token in token_indices:
        token = int(token)
        words.append(tokens[token])
    return ' '.join(words)

def return_tokens(file=False):
    if file:
        return l1
    return tokens