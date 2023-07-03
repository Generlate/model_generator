import os
import torch
from torch.utils.data import Dataset


class TrainingDataLoader(Dataset):
    def __init__(SELF, data_directory, number_of_files=None):
        # Sorted file paths with limit
        FILE_PATHS = [os.path.join(data_directory, FILE_NAME) for FILE_NAME in
                      sorted(os.listdir(data_directory))][:number_of_files]
        SELF.FILE_CONTENTS = SELF.load_file_contents(FILE_PATHS)

    def __len__(SELF):
        return len(SELF.FILE_CONTENTS)

    def __getitem__(SELF, index):
        return torch.tensor(SELF.FILE_CONTENTS[index])  # Return as a tensor

    def load_file_contents(SELF, file_paths):
        FILE_CONTENTS = []
        for FILE_PATH in file_paths:
            with open(FILE_PATH, 'r') as FILE:
                # Read the third through tenth lines
                LINES = FILE.readlines()[2:10]
                CONTENT = "".join(LINES)
                FORMATTED_CONTENT = SELF.format_content(CONTENT)
                FILE_CONTENTS.append(FORMATTED_CONTENT)
        return FILE_CONTENTS

    def format_content(SELF, content):
        LINES = content.split('\n')
        FORMATTED_LINES = [list(map(round, map(float, LINE.split())))
                           for LINE in LINES if LINE.strip()]
        return [VAL for SUBLIST in FORMATTED_LINES for VAL in SUBLIST]
