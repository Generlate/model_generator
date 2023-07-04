import torch
from utils.training_data_loader import TrainingDataLoader

# Specify where the training boxes are stored and how many to load.
data_directory = './datasets/austens_boxes/training/'
number_of_files = 60

# Apply the class that loads and formats the box data.
TRAINING_DATASET = TrainingDataLoader(data_directory, number_of_files)

# Get numbers from the files and convert to tensor
TRAINING_NUMBER_LISTS = [torch.tensor([LIST[INDEX]
                                       for LIST in
                                       TRAINING_DATASET.file_contents
                                       if len(LIST) > INDEX])
                         for INDEX in range(24)]

TRAINING_NUMBER_LISTS_FLOAT32 = [TENSOR.to(torch.float32)
                                 for TENSOR in TRAINING_NUMBER_LISTS]

# Combine tensors into a single tensor
TRAINING_COMBINED_TENSOR = torch.stack(TRAINING_NUMBER_LISTS_FLOAT32, dim=0)
