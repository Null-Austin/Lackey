import subprocess
import os
import json

def path(path):
    return os.path.join(os.path.dirname(__file__), path)

# Download and prepare data
subprocess.run(['curl','-o',path('data/english10k.txt'),'https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english.txt'])
subprocess.run(['curl','-o',path('data/englishdict.txt'),'https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt'])
subprocess.run(['python3', path('data/transform-data.py')])