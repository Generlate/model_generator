import torch
import torch.nn as nn


# Define the neural network structure. More hidden layers had negligent effect on loss.
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.hidden1 = nn.Linear(60, 80)  # Neural network layers
        self.hidden2 = nn.Linear(80, 80)
        self.hidden3 = nn.Linear(80, 80)
        self.output = nn.Linear(80, 1)

    def forward(self, x):
        x = torch.relu(self.hidden1(x))  # and applying activation function.
        x = torch.relu(self.hidden2(x))
        x = torch.relu(self.hidden3(x))
        x = self.output(x)
        return x
