import torch
import torch.nn as nn


# Define the neural network architecture
class SimpleFeedForwardNN(nn.Module):
    def __init__(self):
        super(SimpleFeedForwardNN, self).__init__()

        # Manually set the initial weights and biases
        weight_init = torch.tensor([[0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1]])
        bias_init = torch.tensor([0.0, 0.0, 0.0])

        self.fullyconnected = nn.Linear(3, 3)  # Input layer: input 3 features, output 3 features.
        self.fullyconnected.weight = nn.Parameter(weight_init)
        self.fullyconnected.bias = nn.Parameter(bias_init)


    def forward(self, f):
        print("f: ", f)
        print("Weight:", self.fullyconnected.weight)
        print("Bias:", self.fullyconnected.bias)
        f = (self.fullyconnected(f))  # Apply ReLU activation
        print("f: ", f)
        return f


# Create an instance of the neural network
model = SimpleFeedForwardNN()

# Create a sample batch of input objects
input_batch = torch.tensor([[1, 2, 3],
                            [2, 4, 1]], dtype=torch.float32)

# Pass the input batch through the neural network
output_object = model(input_batch)

# Print the output object
print("output batch: ", output_object)
