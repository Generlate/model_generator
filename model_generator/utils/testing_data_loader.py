import os
import torch
from torch.utils.data import Dataset


class TestingDataLoader(Dataset):
    def __init__(self, data_directory, number_of_files=None):
        # Sorted file names with limit
        file_names = sorted(os.listdir(data_directory))[:number_of_files]
        self.file_paths = [os.path.join(data_directory, file_name)
                           for file_name in file_names]

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, index):
        file_path = self.file_paths[index]
        file_contents = self.load_file_contents(file_path)
        # Return file contents as a tensor
        return torch.tensor(file_contents, dtype=torch.float32)

    def load_file_contents(SELF, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()[2:10]
            content = "".join(lines)
            formatted_content = SELF.format_content(content)
        return formatted_content

    def format_content(SELF, content):
        lines = content.split('\n')
        formatted_lines = [list(map(round, map(float, line.split())))
                           for line in lines if line.strip()]
        flattened_list = [val for sublist in formatted_lines
                          for val in sublist]
        reshaped_array = torch.tensor(flattened_list).reshape(-1, 1)
        return reshaped_array
