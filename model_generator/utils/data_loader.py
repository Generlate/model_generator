import os
import torch
from torch.utils.data import Dataset


class TrainingDataLoader(Dataset):
    def __init__(self, training_data_directory, training_number_of_files):
        # The sorted file paths limited to the number specified.
        file_paths = [os.path.join(training_data_directory, file_name) for file_name in
                      sorted(os.listdir(training_data_directory))][:training_number_of_files]
        self.file_contents = self.load_file_contents(file_paths)

    def __len__(self):
        return len(self.file_contents)

    def __getitem__(self, index):
        # Return as a tensor.
        return torch.tensor(self.file_contents[index])

    def load_file_contents(self, file_paths):
        file_contents = []
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                lines = file.readlines()[2:10]
                content = "".join(lines)
                organized_content = self.organize_content(content)
                file_contents.append(organized_content)
        return file_contents

    def organize_content(self, content):
        lines = content.split('\n')
        organized_lines = [list(map(round, map(float, line.split())))
                           for line in lines if line.strip()]
        return [val for sublist in organized_lines for val in sublist]


class TestingDataLoader(Dataset):
    def __init__(self, testing_data_directory, testing_number_of_files):
        # The sorted file paths limited to the number specified.
        file_names = sorted(os.listdir(testing_data_directory))[
            :testing_number_of_files]
        self.file_paths = [os.path.join(testing_data_directory, file_name)
                           for file_name in file_names]

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, index):
        file_path = self.file_paths[index]
        file_contents = self.load_file_contents(file_path)
        # Return file contents as a tensor.
        return torch.tensor(file_contents, dtype=torch.float32)

    def load_file_contents(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()[2:10]
            content = "".join(lines)
            formatted_content = self.organize_content(content)
        return formatted_content

    def organize_content(self, content):
        lines = content.split('\n')
        organized_lines = [list(map(round, map(float, line.split())))
                           for line in lines if line.strip()]
        flattened_list = [val for sublist in organized_lines
                          for val in sublist]
        reshaped_array = torch.tensor(flattened_list).reshape(-1, 1)
        return reshaped_array
