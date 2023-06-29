import os
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, data_dir):
        self.file_list = sorted(os.listdir(data_dir))  # Sort the file list
        self.file_contents = self.load_file_contents(data_dir)

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        return self.file_contents[idx]

    def load_file_contents(self, data_dir):
        file_contents = []
        for file_name in self.file_list:
            file_path = os.path.join(data_dir, file_name)
            with open(file_path, 'r') as file:
                lines = file.readlines()[2:10]  # Read the third through tenth lines
                content = "".join(lines)
                formatted_content = self.format_content(content)
                file_contents.append(formatted_content)
        return file_contents

    def format_content(self, content):
        lines = content.split('\n')
        formatted_lines = [list(map(float, line.split())) for line in lines if line.strip()]
        return [val for sublist in formatted_lines for val in sublist]

data_dir = '../Datasets/AustensBoxes/'
dataset = CustomDataset(data_dir)

# Access file contents from the dataset
print("Content of the first file:", dataset.file_contents[0])

# Get numbers from dataset.file_contents
number_lists = [[lst[index] for lst in dataset.file_contents if len(lst) > index] for index in range(24)]

for i, numbers in enumerate(number_lists):
    print(f"{i+1}th numbers:", numbers)
