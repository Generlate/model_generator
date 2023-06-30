import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset
import training_data_loader
import testing_data_loader

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

# Create an instance of the neural network
model = NeuralNetwork()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop 
training_input = training_data_loader.Training_combined_tensor

testing_data = testing_data_loader.Testing_combined_tensor
print("Test Output:")
print(testing_data)


num_epochs = 3
testing_data_iter = iter(testing_data)
for epoch in range(num_epochs):
    # Get the next testing data tensor
    testing_data_tensor = next(testing_data_iter)

    # Forward pass
    output = model(training_input)
    loss = criterion(output, testing_data_tensor)  # Using output as both the input and target for unsupervised learning

    # Print the loss every epoch
    print(f"Epoch: {epoch+1}, Loss: {loss.item()}")

array = output.detach().numpy().flatten()

x_list = []
for x in range(len(array)):
    if x % 3 == 0:
        x_list.append(array[x] * 20)

y_list = []
for y in range(len(array)):
    if y % 3 in [1]:
        y_list.append(array[y] * 20)

z_list = []
for z in range(len(array)):
    if z % 3 in [2]:
        z_list.append(array[z] * 20)

# plot the .off
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
