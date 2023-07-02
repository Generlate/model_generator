import os
import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, data_directory, num_files=None):
        file_paths = [os.path.join(data_directory, file_name) for file_name in sorted(os.listdir(data_directory))][:num_files]  # Sorted file paths with limit
        self.file_contents = self.load_file_contents(file_paths)

    def __len__(self):
        return len(self.file_contents)

    def __getitem__(self, idx):
        return torch.tensor(self.file_contents[idx])  # Return as a tensor

    def load_file_contents(self, file_paths):
        file_contents = []
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                lines = file.readlines()[2:10]  # Read the third through tenth lines
                content = "".join(lines)
                formatted_content = self.format_content(content)
                file_contents.append(formatted_content)
        return file_contents

    def format_content(self, content):
        lines = content.split('\n')
        formatted_lines = [list(map(round, map(float, line.split()))) for line in lines if line.strip()]
        return [val for sublist in formatted_lines for val in sublist]

data_directory = './Datasets/AustensBoxes/training/'
num_files_to_load = 60  # Specify the number of files to load
Training_dataset = CustomDataset(data_directory, num_files=num_files_to_load)

# Get numbers from dataset.file_contents
Training_number_lists = [torch.tensor([lst[index] for lst in Training_dataset.file_contents if len(lst) > index]) for index in range(24)]  # Convert to tensor

Training_number_lists_float32 = [tensor.to(torch.float32) for tensor in Training_number_lists]

# Combine number_lists into a single tensor
Training_combined_tensor = torch.stack(Training_number_lists_float32, dim=0)
