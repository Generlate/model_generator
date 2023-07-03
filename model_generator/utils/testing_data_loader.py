import os
import torch
from torch.utils.data import Dataset


class TestingDataLoader(Dataset):
    def __init__(SELF, data_directory, number_of_files=None):
        # Sorted file names with limit
        FILE_NAMES = sorted(os.listdir(data_directory))[:number_of_files]
        SELF.FILE_PATHS = [os.path.join(data_directory, FILE_NAME)
                           for FILE_NAME in FILE_NAMES]

    def __len__(SELF):
        return len(SELF.FILE_PATHS)

    def __getitem__(SELF, index):
        FILE_PATH = SELF.FILE_PATHS[index]
        FILE_CONTENTS = SELF.load_file_contents(FILE_PATH)
        # Return file contents as a tensor
        return torch.tensor(FILE_CONTENTS, dtype=torch.float32)

    def load_file_contents(SELF, file_path):
        with open(file_path, 'r') as FILE:
            # Read the third through tenth lines
            LINES = FILE.readlines()[2:10]
            CONTENT = "".join(LINES)
            FORMATTED_CONTENT = SELF.format_content(CONTENT)
        return FORMATTED_CONTENT

    def format_content(SELF, content):
        LINES = content.split('\n')
        FORMATTED_LINES = [list(map(round, map(float, LINE.split())))
                           for LINE in LINES if LINE.strip()]
        FLATTENED_LIST = [VAL for SUBLIST in FORMATTED_LINES
                          for VAL in SUBLIST]
        RESHAPED_ARRAY = torch.tensor(FLATTENED_LIST).reshape(-1, 1)
        return RESHAPED_ARRAY
