import torch
from utils.training_data_loader import TrainingDataLoader

data_directory = './datasets/austens_boxes/training/'
number_of_files = 60  # Specify the number of files to load
TRAINING_DATASET = TrainingDataLoader(data_directory, number_of_files)

# Get numbers from dataset.file_contents and convert to tensor
TRAINING_NUMBER_LISTS = [torch.tensor([LIST[INDEX]
                                       for LIST in
                                       TRAINING_DATASET.FILE_CONTENTS
                                       if len(LIST) > INDEX])
                         for INDEX in range(24)]

TRAINING_NUMBER_LISTS_FLOAT32 = [TENSOR.to(torch.float32)
                                 for TENSOR in TRAINING_NUMBER_LISTS]

# Combine number_lists into a single tensor
TRAINING_COMBINED_TENSOR = torch.stack(TRAINING_NUMBER_LISTS_FLOAT32, dim=0)
