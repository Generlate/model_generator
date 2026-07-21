"""Formats the dataset to the proper format for the neural network to process."""

from typing import List

import torch
from utils.data_loader import TestingDataLoader, TrainingDataLoader

# Specify where the training and testing boxes are stored and how many to load.
training_data_directory: str = "./datasets/austens_boxes/training/"
testing_data_directory: str = "./datasets/austens_boxes/testing/"
training_number_of_files: int = 60
testing_number_of_files: int = 10

# Apply the class that loads and formats the box data.
TRAINING_DATASET: TrainingDataLoader = TrainingDataLoader(
    training_data_directory, training_number_of_files
)
TESTING_DATASET: TestingDataLoader = TestingDataLoader(
    testing_data_directory, testing_number_of_files
)


# Get numbers from the files and convert to tensor.
TRAINING_NUMBER_LISTS: List[torch.Tensor] = [
    torch.tensor(
        [
            LIST[INDEX]
            for LIST in TRAINING_DATASET.file_contents
            if len(LIST) > INDEX
        ]
    )
    for INDEX in range(24)
]

TRAINING_NUMBER_LISTS_FLOAT32: List[torch.Tensor] = [
    TENSOR.to(torch.float32) for TENSOR in TRAINING_NUMBER_LISTS
]


# Get testing tensors for each file.
TESTING_TENSORS: List[torch.Tensor] = [
    TESTING_DATASET[INDEX] for INDEX in range(len(TESTING_DATASET))
]

# Combine tensors into a single tensor.
TRAINING_COMBINED_TENSOR: torch.Tensor = torch.stack(
    TRAINING_NUMBER_LISTS_FLOAT32, dim=0
)
TESTING_COMBINED_TENSOR: torch.Tensor = torch.stack(TESTING_TENSORS, dim=0)
