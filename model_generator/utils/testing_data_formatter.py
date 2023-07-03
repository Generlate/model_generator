import torch
from utils.testing_data_loader import TestingDataLoader


data_directory = './datasets/austens_boxes/testing/'
number_of_files = 10  # Specify the number of files to load
TESTING_DATASET = TestingDataLoader(data_directory, number_of_files)

# Get tensors for each file
TESTING_TENSORS = [TESTING_DATASET[INDEX]
                   for INDEX in range(len(TESTING_DATASET))]

# Combine tensors into a single tensor
TESTING_COMBINED_TENSOR = torch.stack(TESTING_TENSORS, dim=0)
