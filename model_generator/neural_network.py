import torch
import torch.nn as nn


# Define the neural network architecture
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.hidden1 = nn.Linear(60, 80)  # First hidden layer
        self.hidden2 = nn.Linear(80, 80)  # Second hidden layer
        self.hidden3 = nn.Linear(80, 80)  # Third hidden layer
        self.output = nn.Linear(80, 1)  # Output layer

    def forward(self, x):
        x = torch.relu(self.hidden1(x))
        x = torch.relu(self.hidden2(x))
        x = torch.relu(self.hidden3(x))
        x = self.output(x)
        return x
