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

num_epochs = 3
testing_data_iter = iter(testing_data)
for epoch in range(num_epochs):
    # Get the next testing data tensor
    testing_data_tensor = next(testing_data_iter)

    # Forward pass
    output = model(training_input)
    loss = criterion(output, testing_data_tensor)  # Using output as both the input and target for unsupervised learning

    # Print the loss every epoch
    # print(f"Epoch: {epoch+1}, Loss: {loss.item()}")

array = output.detach().numpy().flatten()


# format to .off
formatted_array = 'OFF\n8 6 0\n'
for i, value in enumerate(array):
    formatted_array += str(value * 22) + ' '
    if (i + 1) % 3 == 0:
        formatted_array += '\n'

additional_string = '''4 0 1 2 3
4 1 5 6 2
4 5 4 7 6
4 4 0 3 7
4 3 2 6 7
4 4 5 1 0'''

formatted_array += additional_string

file_path = "generated_box.off"  # Specify the base file path where you want to save the .off file
file_exists = os.path.exists(file_path)

# Check if the file already exists
if file_exists:
    # Find the next available file name by incrementing a counter
    file_counter = 1
    while file_exists:
        file_name, file_extension = os.path.splitext(file_path)
        incremented_file_path = f"{file_name}_{file_counter}{file_extension}"
        file_exists = os.path.exists(incremented_file_path)
        file_counter += 1

    file_path = incremented_file_path

# Save the .off file
with open(file_path, 'w') as file:
    file.write(formatted_array)

print("File generated successfully. Saved as:", file_path)