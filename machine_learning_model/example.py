import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Define the neural network architecture
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.hidden = nn.Linear(3, 5)  # Hidden layer with 5 units
        self.output = nn.Linear(5, 1)  # Output layer

    def forward(self, x):
        x = torch.relu(self.hidden(x))
        x = self.output(x)
        return x

# Create an instance of the neural network
model = NeuralNetwork()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
training_input = torch.tensor([[-3.29, -3.48, -4.87], [-1.35, -4.01, -0.98], [-1.41, -3.14, -4.72], [3.29, 3.48, 4.87], [-1.35, -4.01, -0.98], [-1.41, -3.14, -4.72], [3.29, 3.48, 4.87], [1.35, 4.01, 0.98],
                           [-1.41, -3.14, -4.72], [-3.29, -3.48, -4.87], [1.35, 4.01, 0.98], [-1.41, -3.14, -4.72], [-3.29, -3.48, -4.87], [-1.35, -4.01, -0.98], [1.41, 3.14, 4.72], [3.29, 3.48, 4.87], 
                           [-1.35, -4.01, -0.98], [1.41, 3.14, 4.72], [3.29, 3.48, 4.87], [1.35, 4.01, 0.98], [1.41, 3.14, 4.72], [-3.29, -3.48, -4.87], [1.35, 4.01, 0.98], [1.41, 3.14, 4.72]], dtype=torch.float32)
target = torch.tensor([[3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3], 
                        [3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3],
                        [3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3], [3, 1, 2], [4, 2, 3], ], dtype=torch.float32)

# Test the trained model
test_input = torch.tensor([[-4.67, -4.91, -1.63], [-1.58, -1.15, -3.94], [-1.02, -3.53, -0.70], [4.67, 4.91, 1.63], [-1.58, -1.15, -3.94], [-1.02, -3.53, -0.70], [4.67, 4.91, 1.63], [1.58, 1.15, 3.94],
                           [-1.02, -3.53, -0.70], [-4.67, -4.91, -1.63], [1.58, 1.15, 3.94], [-1.02, -3.53, -0.70], [-4.67, -4.91, -1.63], [-1.58, -1.15, -3.94], [1.02, 3.53, 0.70], [4.67, 4.91, 1.63], 
                           [-1.58, -1.15, -3.94], [1.02, 3.53, 0.70], [4.67, 4.91, 1.63], [1.58, 1.15, 3.94], [1.02, 3.53, 0.70], [-4.67, -4.91, -1.63], [1.58, 1.15, 3.94], [1.02, 3.53, 0.70]], dtype=torch.float32)

num_epochs = 100
for epoch in range(num_epochs):
    # Forward pass
    output = model(training_input)
    loss = criterion(output, target)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print the loss every 100 epochs
    if (epoch + 1) % 10 == 0:
        print(f"Epoch: {epoch+1}, Loss: {loss.item()}")


test_output = model(test_input)
print("Test Output:")
print(test_output)

array = test_output.detach().numpy().flatten()

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