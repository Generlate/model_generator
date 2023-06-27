import torch
import torch.nn as nn
import matplotlib.pyplot as plt
# import data_loader


# Define the neural network architecture
class SimpleFeedForwardNN(nn.Module):
    def __init__(self):
        super(SimpleFeedForwardNN, self).__init__()
        self.fullyconnected1 = nn.Linear(24, 24)  # Input layer: 24 features input, 24 features output
        self.fullyconnected3 = nn.Linear(24, 24)  # Output layer: 24 features input, 24 features output

    def forward(self, a):
        a = torch.relu(self.fullyconnected1(a))  # Apply ReLU activation to the first layer
        a = self.fullyconnected3(a)              # Output layer, no activation function
        return a


# Create an instance of the neural network
model = SimpleFeedForwardNN()

# Create a sample batch of input objects
input_batch = torch.tensor([[-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            [-1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, -1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, -1.2659623945887473,
                            -1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, -4.109770277877468, 1.2659623945887473,
                            1.4022106939553134, 4.109770277877468, 1.2659623945887473,
                            -1.4022106939553134, 4.109770277877468, 1.2659623945887473],
                            ])  # this is where the data loader puts batches


# Pass the input batch through the neural network
output_object = model(input_batch)

# Aggregate the output across the sample dimension
aggregated_output = torch.mean(output_object, dim=0, keepdim=True)

# Print the output object
print(aggregated_output)

# Reformat aggregated_output to three arrays for x, y and z
flattened_tensor = aggregated_output.flatten()
array = flattened_tensor.tolist()

x_list = []
for x in range(len(array)):
    if x % 3 == 0:
        x_list.append(array[x])

y_list = []
for y in range(len(array)):
    if y % 3 in [1]:
        y_list.append(array[y])

z_list = []
for z in range(len(array)):
    if z % 3 in [2]:
        z_list.append(array[z])


#plot the .off
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D coordinates
ax.scatter(x_list, y_list, z_list)


# Set labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
