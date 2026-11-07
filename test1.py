import torch
import torch.nn as nn


print('hello bro')
layer = nn.Linear(3, 2)
print(layer.weight)

for i in range(30):
    print(i)