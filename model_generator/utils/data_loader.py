"""Module to get data from a directory and convert it to a python dataset."""

import os
from typing import List

import torch
from torch.utils.data import Dataset


class TrainingDataLoader(Dataset):
    """Allows a training dataset to be created from a directory of files."""

    def __init__(
        self, training_data_directory: str, training_number_of_files: int
    ) -> None:
        """Initializes a Dataset by loading files from a directory."""
        # The sorted file paths limited to the number specified.
        file_paths: List[str] = [
            os.path.join(training_data_directory, file_name)
            for file_name in sorted(os.listdir(training_data_directory))
        ][:training_number_of_files]
        self.file_contents = self.load_file_contents(file_paths)

    def __len__(self) -> int:
        """Returns the dataset's length."""
        return len(self.file_contents)

    def __getitem__(self, index: int) -> torch.Tensor:
        """Return as a tensor."""
        return torch.tensor(self.file_contents[index])

    def load_file_contents(self, file_paths: List[str]) -> List[List[int]]:
        """Loads file contents."""
        file_contents: List[List[int]] = []
        for file_path in file_paths:
            with open(file_path, "r") as file:
                lines: List[str] = file.readlines()[2:10]
                content: str = "".join(lines)
                organized_content: List[int] = self.organize_content(content)
                file_contents.append(organized_content)
        return file_contents

    def organize_content(self, content: str) -> List[int]:
        """Organize the dataset."""
        lines: List[str] = content.split("\n")
        organized_lines: List[List[int]] = [
            list(map(round, map(float, line.split())))
            for line in lines
            if line.strip()
        ]
        return [val for sublist in organized_lines for val in sublist]


class TestingDataLoader(Dataset):
    """Allows a testing dataset to be created from a directory of files."""

    def __init__(
        self, testing_data_directory: str, testing_number_of_files: int
    ) -> None:
        """To fill."""
        file_names: List[str] = sorted(os.listdir(testing_data_directory))[
            :testing_number_of_files
        ]
        self.file_paths: List[str] = [
            os.path.join(testing_data_directory, file_name)
            for file_name in file_names
        ]

    def __len__(self) -> int:
        """Return the dataset's length."""
        return len(self.file_paths)

    def __getitem__(self, index: int) -> torch.Tensor:
        """Return file contents as a tensor."""
        file_path: str = self.file_paths[index]
        file_contents: torch.Tensor = self.load_file_contents(file_path)
        return torch.tensor(file_contents, dtype=torch.float32)

    def load_file_contents(self, file_path: str) -> torch.Tensor:
        """Loads file contents."""
        with open(file_path, "r") as file:
            lines: List[str] = file.readlines()[2:10]
            content: str = "".join(lines)
            formatted_content: torch.Tensor = self.organize_content(content)
        return formatted_content

    def organize_content(self, content: str) -> torch.Tensor:
        """Organize the dataset."""
        lines: List[str] = content.split("\n")
        organized_lines: List[List[int]] = [
            list(map(round, map(float, line.split())))
            for line in lines
            if line.strip()
        ]
        flattened_list: List[int] = [
            val for sublist in organized_lines for val in sublist
        ]
        reshaped_array: torch.Tensor = torch.tensor(flattened_list).reshape(
            -1, 1
        )
        return reshaped_array
