#!/usr/bin/env python3

""" Runs a formatted dataset through a neural network, formats the output to be viewed as a 3d object and file name."""

import os
import torch.nn as nn
import torch.optim as optim
import utils.data_formatter
import utils.data_loader
from utils.neural_network import NeuralNetwork

if __name__ == "__main__":
    # Create an instance of the neural network.
    model = NeuralNetwork()

    # Define the loss function and optimizer.
    CRITERION = nn.MSELoss()
    OPTIMIZER = optim.SGD(model.parameters(), lr=0.01)

    # Load the datasets.
    TRAINING_INPUT = utils.data_formatter.TRAINING_COMBINED_TENSOR
    TESTING_INPUT = utils.data_formatter.TESTING_COMBINED_TENSOR

    # Set number of epochs. I found three to give the lowest loss score.
    NUMBER_OF_EPOCHS = 3
    TESTING_DATA_ITERATOR = iter(TESTING_INPUT)

    # The training loop.
    for EPOCH in range(NUMBER_OF_EPOCHS):
        # Get the next testing data tensor.
        TESTING_DATA_TENSOR = next(TESTING_DATA_ITERATOR)

        # Generate box coordinates.
        OUTPUT = model(TRAINING_INPUT)

        # Compare the generated coordinates against the test coordinates.
        LOSS = CRITERION(OUTPUT, TESTING_DATA_TENSOR)

        # Print the loss every epoch.
        # print(f"Epoch: {epoch+1}, Loss: {loss.item()}")

    # List the generated coordinates.
    ARRAY = OUTPUT.detach().numpy().flatten()

    # Format to .off.
    FORMATTED_ARRAY = "OFF\n8 6 0\n"
    for i, VALUE in enumerate(ARRAY):
        FORMATTED_ARRAY += str(VALUE * 22) + " "
        if (i + 1) % 3 == 0:
            FORMATTED_ARRAY += "\n"

    ADDITIONAL_STRING = """4 0 1 2 3
    4 1 5 6 2
    4 5 4 7 6
    4 4 0 3 7
    4 3 2 6 7
    4 4 5 1 0"""

    FORMATTED_ARRAY += ADDITIONAL_STRING

    file_path = "./generated_boxes/generated_box.off"

    # Check if the file already exists.
    FILE_EXISTS = os.path.exists(file_path)
    if FILE_EXISTS:
        # Find the next available file name by incrementing a counter.
        FILE_COUNTER = 1
        while FILE_EXISTS:
            FILE_NAME, FILE_EXTENSION = os.path.splitext(file_path)
            INCREMENTED_FILE_PATH = (
                f"{FILE_NAME}_{FILE_COUNTER}{FILE_EXTENSION}"
            )
            FILE_EXISTS = os.path.exists(INCREMENTED_FILE_PATH)
            FILE_COUNTER += 1

        file_path = INCREMENTED_FILE_PATH

    # Save the .off file.
    with open(file_path, "w") as FILE:
        FILE.write(FORMATTED_ARRAY)

    print("File generated successfully. Saved as:", file_path)

# todo: add docs with Sphinx
# todo: add a --version, --help and cli_args function
