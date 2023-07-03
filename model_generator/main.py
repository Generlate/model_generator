import os
import numpy
import torch.nn as nn
import torch.optim as optim
import utils.training_data_formatter
import utils.testing_data_formatter
from utils.neural_network import NeuralNetwork


# Create an instance of the neural network
MODEL = NeuralNetwork()

# Define the loss function and optimizer
CRITERION = nn.MSELoss()
OPTIMIZER = optim.SGD(MODEL.parameters(), lr=0.01)

# Training loop
TRAINING_INPUT = utils.training_data_formatter.TRAINING_COMBINED_TENSOR

TESTING_DATA = utils.testing_data_formatter.TESTING_COMBINED_TENSOR

NUMBER_OF_EPOCHS = 3
TESTING_DATA_ITERATOR = iter(TESTING_DATA)
for EPOCH in range(NUMBER_OF_EPOCHS):
    # Get the next testing data tensor
    TESTING_DATA_TENSOR = next(TESTING_DATA_ITERATOR)

    # Forward pass
    OUTPUT = MODEL(TRAINING_INPUT)
    # Using output as both the input and target for unsupervised learning
    LOSS = CRITERION(OUTPUT, TESTING_DATA_TENSOR)

    # Print the loss every epoch
    # print(f"Epoch: {epoch+1}, Loss: {loss.item()}")

ARRAY = OUTPUT.detach().numpy().flatten()

# format to .off
FORMATTED_ARRAY = 'OFF\n8 6 0\n'
for i, VALUE in enumerate(ARRAY):
    FORMATTED_ARRAY += str(VALUE * 22) + ' '
    if (i + 1) % 3 == 0:
        FORMATTED_ARRAY += '\n'

ADDITIONAL_STRING = '''4 0 1 2 3
4 1 5 6 2
4 5 4 7 6
4 4 0 3 7
4 3 2 6 7
4 4 5 1 0'''

FORMATTED_ARRAY += ADDITIONAL_STRING

# Specify the base file path where you want to save the .off file
file_path = "./generated_boxes/generated_box.off"
FILE_EXISTS = os.path.exists(file_path)

# Check if the file already exists
if FILE_EXISTS:
    # Find the next available file name by incrementing a counter
    FILE_COUNTER = 1
    while FILE_EXISTS:
        FILE_NAME, FILE_EXTENSION = os.path.splitext(file_path)
        INCREMENTED_FILE_PATH = f"{FILE_NAME}_{FILE_COUNTER}{FILE_EXTENSION}"
        FILE_EXISTS = os.path.exists(INCREMENTED_FILE_PATH)
        FILE_COUNTER += 1

    file_path = INCREMENTED_FILE_PATH

# Save the .off file
with open(file_path, 'w') as FILE:
    FILE.write(FORMATTED_ARRAY)

print("File generated successfully. Saved as:", file_path)
