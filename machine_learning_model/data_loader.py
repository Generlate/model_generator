import os
import torch
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.file_list = os.listdir(data_dir)

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        file_path = os.path.join(self.data_dir, self.file_list[idx])
        # Load your .off file and preprocess it if needed
        # Return the preprocessed data and its label
        return data, label

data_dir = 'path/to/your/data_directory'
dataset = CustomDataset(data_dir)

batch_size = 32
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

for batch_data, batch_labels in dataloader:
    # Your training code here

