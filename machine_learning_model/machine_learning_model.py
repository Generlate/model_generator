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
input_batch = torch.tensor([[-3.29, -1.35, -1.41,
                            3.29, -1.35, -1.41,
                            3.29, 1.35, -1.41,
                            -3.29, 1.35, -1.41,
                            -3.29, -1.35, 1.41,
                            3.29, -1.35, 1.41,
                            3.29, 1.35, 1.41,
                            -3.29, 1.35, 1.41],
                            [-3.48, -4.01, -3.14,
                            3.48, -4.01, -3.14,
                            3.48, 4.01, -3.14,
                            -3.48, 4.01, -3.14,
                            -3.48, -4.01, 3.14,
                            3.48, -4.01, 3.14,
                            3.48, 4.01, 3.14,
                            -3.48, 4.01, 3.14],
                            [-4.87, -0.98, -4.72,
                            4.87, -0.98, -4.72,
                            4.87, 0.98, -4.72,
                            -4.87, 0.98, -4.72,
                            -4.87, -0.98, 4.72,
                            4.87, -0.98, 4.72,
                            4.87, 0.98, 4.72,
                            -4.87, 0.98, 4.72],
                            [-4.67, -1.58, -1.02,
                            4.67, -1.58, -1.02,
                            4.67, 1.58, -1.02,
                            -4.67, 1.58, -1.02,
                            -4.67, -1.58, 1.02,
                            4.67, -1.58, 1.02,
                            4.67, 1.58, 1.02,
                            -4.67, 1.58, 1.02],
                            [-4.91, -1.15, -3.53,
                            4.91, -1.15, -3.53,
                            4.91, 1.15, -3.53,
                            -4.91, 1.15, -3.53,
                            -4.91, -1.15, 3.53,
                            4.91, -1.15, 3.53,
                            4.91, 1.15, 3.53,
                            -4.91, 1.15, 3.53],
                            [-1.63, -3.94, -0.70,
                            1.63, -3.94, -0.70,
                            1.63, 3.94, -0.70,
                            -1.63, 3.94, -0.70,
                            -1.63, -3.94, 0.70,
                            1.63, -3.94, 0.70,
                            1.63, 3.94, 0.70,
                            -1.63, 3.94, 0.70],
                            [-3.86, -2.71, -0.66,
                            3.86, -2.71, -0.66,
                            3.86, 2.71, -0.66,
                            -3.86, 2.71, -0.66,
                            -3.86, -2.71, 0.66,
                            3.86, -2.71, 0.66,
                            3.86, 2.71, 0.66,
                            -3.86, 2.71, 0.66],
                            [-1.57, -2.21, -1.41,
                            1.57, -2.21, -1.41,
                            1.57, 2.21, -1.41,
                            -1.57, 2.21, -1.41,
                            -1.57, -2.21, 1.41,
                            1.57, -2.21, 1.41,
                            1.57, 2.21, 1.41,
                            -1.57, 2.21, 1.41],
                            [-4.71, -0.75, -0.87,
                            4.71, -0.75, -0.87,
                            4.71, 0.75, -0.87,
                            -4.71, 0.75, -0.87,
                            -4.71, -0.75, 0.87,
                            4.71, -0.75, 0.87,
                            4.71, 0.75, 0.87,
                            -4.71, 0.75, 0.87],
                            [-1.30, -1.79, -1.07,
                            1.30, -1.79, -1.07,
                            1.30, 1.79, -1.07,
                            -1.30, 1.79, -1.07,
                            -1.30, -1.79, 1.07,
                            1.30, -1.79, 1.07,
                            1.30, 1.79, 1.07,
                            -1.30, 1.79, 1.07],
                            [-4.63, -2.12, -1.04,
                            4.63, -2.12, -1.04,
                            4.63, 2.12, -1.04,
                            -4.63, 2.12, -1.04,
                            -4.63, -2.12, 1.04,
                            4.63, -2.12, 1.04,
                            4.63, 2.12, 1.04,
                            -4.63, 2.12, 1.04],
                            [-1.33, -3.21, -4.17,
                            1.33, -3.21, -4.17,
                            1.33, 3.21, -4.17,
                            -1.33, 3.21, -4.17,
                            -1.33, -3.21, 4.17,
                            1.33, -3.21, 4.17,
                            1.33, 3.21, 4.17,
                            -1.33, 3.21, 4.17]])  # this is where the data loader puts batches


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
