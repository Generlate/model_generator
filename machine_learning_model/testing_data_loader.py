import os
import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, data_directory, num_files=None):
        file_names = sorted(os.listdir(data_directory))[:num_files]  # Sorted file names with limit
        self.file_paths = [os.path.join(data_directory, file_name) for file_name in file_names]

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        file_path = self.file_paths[idx]
        file_contents = self.load_file_contents(file_path)
        return torch.tensor(file_contents)  # Return file contents as a tensor

    def load_file_contents(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()[2:10]  # Read the third through tenth lines
            content = "".join(lines)
            formatted_content = self.format_content(content)
        return formatted_content

    def format_content(self, content):
        lines = content.split('\n')
        formatted_lines = [list(map(round, map(float, line.split()))) for line in lines if line.strip()]
        flattened_list = [val for sublist in formatted_lines for val in sublist]
        reshaped_array = torch.tensor(flattened_list).reshape(-1, 1)
        return reshaped_array

data_directory = './Datasets/AustensBoxes/testing/'
num_files_to_load = 10  # Specify the number of files to load
Testing_dataset = CustomDataset(data_directory, num_files=num_files_to_load)

# Get tensors for each file
Testing_tensors = [Testing_dataset[idx] for idx in range(len(Testing_dataset))]

Testing_tensors_float32 = [tensor.to(torch.float32) for tensor in Testing_tensors]

# Combine tensors into a single tensor
Testing_combined_tensor = torch.stack(Testing_tensors_float32, dim=0)
