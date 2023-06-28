import torch

m = torch.nn.Linear(3, 3)
input = torch.tensor([[1, 2, 3],
                      [2, 4, 1]], dtype=torch.float32)
weights = torch.tensor([[1.0, 1.0, 1.0]])
m.weight = torch.nn.Parameter(weights)
bias = torch.tensor([[0.0]])
m.bias = torch.nn.Parameter(bias)
output = m(input)
print(output)
