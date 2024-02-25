""" Formats the dataset to the proper format for the neural network to process. """

import torch
from utils.data_loader import TrainingDataLoader, TestingDataLoader


# Specify where the training and testing boxes are stored and how many to load.
training_data_directory = "./datasets/austens_boxes/training/"
testing_data_directory = "./datasets/austens_boxes/testing/"
training_number_of_files = 60
testing_number_of_files = 10

# Apply the class that loads and formats the box data.
TRAINING_DATASET = TrainingDataLoader(
    training_data_directory, training_number_of_files
)
TESTING_DATASET = TestingDataLoader(
    testing_data_directory, testing_number_of_files
)


# Get numbers from the files and convert to tensor.
TRAINING_NUMBER_LISTS = [
    torch.tensor(
        [
            LIST[INDEX]
            for LIST in TRAINING_DATASET.file_contents
            if len(LIST) > INDEX
        ]
    )
    for INDEX in range(24)
]

TRAINING_NUMBER_LISTS_FLOAT32 = [
    TENSOR.to(torch.float32) for TENSOR in TRAINING_NUMBER_LISTS
]


# Get testing tensors for each file.
TESTING_TENSORS = [
    TESTING_DATASET[INDEX] for INDEX in range(len(TESTING_DATASET))
]

# Combine tensors into a single tensor.
TRAINING_COMBINED_TENSOR = torch.stack(TRAINING_NUMBER_LISTS_FLOAT32, dim=0)
TESTING_COMBINED_TENSOR = torch.stack(TESTING_TENSORS, dim=0)
