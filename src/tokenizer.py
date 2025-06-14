# Libaries
import os
import json

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
    tokens = []
    words = s.split()
    for word in words:
        if word in tokens:
            index = tokens.index(word)
            tokens.append(index)
    return tokens

def decode_tokens(tokens):
    words = []
    for token in tokens:
        words.append(tokens[token])
    return ' '.join(words)