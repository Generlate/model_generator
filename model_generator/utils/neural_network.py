""" Takes in tensors and returns new tensors."""

import torch
import torch.nn as nn


# Define the neural network structure. More hidden layers had negligent effect on loss.
class NeuralNetwork(nn.Module):
    """Calls Pytorch functions to process a tensor through a neural network."""

    def __init__(self):
        """Initializes a Neural network with three hidden layers."""
        super(NeuralNetwork, self).__init__()
        self.hidden1 = nn.Linear(60, 80)
        self.hidden2 = nn.Linear(80, 80)
        self.hidden3 = nn.Linear(80, 80)
        self.output = nn.Linear(80, 1)

    def forward(self, x):
        """Applies a relu activation function."""
        x = torch.relu(self.hidden1(x))
        x = torch.relu(self.hidden2(x))
        x = torch.relu(self.hidden3(x))
        x = self.output(x)
        return x
