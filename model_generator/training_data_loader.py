import os
import torch
from torch.utils.data import Dataset


class TrainingDataLoader(Dataset):
    def __init__(self, data_directory, num_files=None):
        # Sorted file paths with limit
        file_paths = [os.path.join(data_directory, file_name) for file_name in
                      sorted(os.listdir(data_directory))][:num_files]
        self.file_contents = self.load_file_contents(file_paths)

    def __len__(self):
        return len(self.file_contents)

    def __getitem__(self, idx):
        return torch.tensor(self.file_contents[idx])  # Return as a tensor

    def load_file_contents(self, file_paths):
        file_contents = []
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                # Read the third through tenth lines
                lines = file.readlines()[2:10]
                content = "".join(lines)
                formatted_content = self.format_content(content)
                file_contents.append(formatted_content)
        return file_contents

    def format_content(self, content):
        lines = content.split('\n')
        formatted_lines = [list(map(round, map(float, line.split())))
                           for line in lines if line.strip()]
        return [val for sublist in formatted_lines for val in sublist]
