import torch
from utils.testing_data_loader import TestingDataLoader

# Specify where the testing boxes are stored and how many to load.
data_directory = './datasets/austens_boxes/testing/'
number_of_files = 10

# Apply the class that loads and formats the box data.
TESTING_DATASET = TestingDataLoader(data_directory, number_of_files)

# Get tensors for each file
TESTING_TENSORS = [TESTING_DATASET[INDEX]
                   for INDEX in range(len(TESTING_DATASET))]

# Combine tensors into a single tensor
TESTING_COMBINED_TENSOR = torch.stack(TESTING_TENSORS, dim=0)
