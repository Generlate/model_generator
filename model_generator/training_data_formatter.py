import torch
from training_data_loader import TrainingDataLoader


data_directory = './datasets/austens_boxes/training/'
num_files_to_load = 60  # Specify the number of files to load
Training_dataset = TrainingDataLoader(data_directory, num_files=num_files_to_load)

# Get numbers from dataset.file_contents and convert to tensor
Training_number_lists = [torch.tensor([lst[index]
                                       for lst in
                                       Training_dataset.file_contents
                                       if len(lst) > index])
                         for index in range(24)]

Training_number_lists_float32 = [tensor.to(torch.float32)
                                 for tensor in Training_number_lists]

# Combine number_lists into a single tensor
Training_combined_tensor = torch.stack(Training_number_lists_float32, dim=0)
