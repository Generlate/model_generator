import torch
from testing_data_loader import TestingDataLoader


data_directory = './datasets/austens_boxes/testing/'
num_files_to_load = 10  # Specify the number of files to load
Testing_dataset = TestingDataLoader(data_directory, num_files=num_files_to_load)

# Get tensors for each file
Testing_tensors = [Testing_dataset[idx] for idx in range(len(Testing_dataset))]

# Combine tensors into a single tensor
Testing_combined_tensor = torch.stack(Testing_tensors, dim=0)
