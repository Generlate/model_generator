import torch
import torch.nn as nn


# Define the neural network architecture
class SimpleFeedForwardNN(nn.Module):
    def __init__(self):
        super(SimpleFeedForwardNN, self).__init__()

        # Manually set the initial weights and biases
        weight_init = torch.tensor([[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])
        bias_init = torch.tensor([[0.0]])

        self.fullyconnected = nn.Linear(12, 1)  # Input layer: input 3 features, output 3 features.
        self.fullyconnected.weight = nn.Parameter(weight_init)
        self.fullyconnected.bias = nn.Parameter(bias_init)


    def forward(self, features):
        features = (self.fullyconnected(features)) 
        return features


# Create an instance of the neural network
model = SimpleFeedForwardNN()

# Create a sample batch of input objects
input_x1 = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], dtype=torch.float32)

# Pass the input batch through the neural network
output_x1 = model(input_x1)

# Print the output object
print(output_x1)



# fix nn.Linear
# fix weights
# fix Bias
# add activation function (ReLU)
# add data loader
# add formatting to .off
# add matplotlib visualization