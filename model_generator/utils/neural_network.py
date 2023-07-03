import torch
import torch.nn as nn


# Define the neural network architecture
class NeuralNetwork(nn.Module):
    def __init__(SELF):
        super(NeuralNetwork, SELF).__init__()
        SELF.HIDDEN1 = nn.Linear(60, 80)  # First hidden layer
        SELF.HIDDEN2 = nn.Linear(80, 80)  # Second hidden layer
        SELF.HIDDEN3 = nn.Linear(80, 80)  # Third hidden layer
        SELF.OUTPUT = nn.Linear(80, 1)  # Output layer

    def forward(SELF, X):
        X = torch.relu(SELF.HIDDEN1(X))
        X = torch.relu(SELF.HIDDEN2(X))
        X = torch.relu(SELF.HIDDEN3(X))
        X = SELF.OUTPUT(X)
        return X
