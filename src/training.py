max_length = 10

import sys
import os
import torch
import torch.nn as nn
import torch.optim as optim

import tokenizer

def path(path):
    return os.path.join(os.path.dirname(__file__), path)

scale = int(tokenizer.return_tokens(True).split('\n')[0])

messageInputs = open(path('./trainingData/messageInputs.txt'),'r', encoding='utf-8').read().split('\n')
messageOutputs = open(path('./trainingData/messageOutputs.txt'),'r', encoding='utf-8').read().split('\n')

messageInputs = [[x / scale for x in tokenizer.encode_tokens(message, max_length=max_length)] for message in messageInputs]
messageOutputs = [[x / scale for x in tokenizer.encode_tokens(message, max_length=max_length)] for message in messageOutputs]

hidden_size = 64

class TextAI(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(max_length, hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_size, max_length)
        self.activation = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.linear1(x))
        return self.activation(self.linear2(x))

model = TextAI()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

inputs = torch.tensor(messageInputs).float()
targets = torch.tensor(messageOutputs).float()

for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

test_input = [x / scale for x in tokenizer.encode_tokens('hello', max_length=max_length)]
tokens = model(torch.tensor(test_input).float())
output_tokens = [max(0, int(round(val.item() * scale))) for val in tokens]
print("model has been trained. test (Hello): \n", tokenizer.decode_tokens(output_tokens))
print('tokens: ', output_tokens)


torch.save(model.state_dict(), os.path.join(os.path.dirname(__file__), './model.pt'))