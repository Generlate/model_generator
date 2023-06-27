import os


class CustomDataset:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.file_list = sorted(os.listdir(data_dir))  # Sort the file list

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        file_path = os.path.join(self.data_dir, self.file_list[idx])
        # Load your .off file and preprocess it if needed
        # Return the preprocessed data
        with open(file_path, 'r') as file:
            data = file.read()
            print("File:", file_path)
            print("Content:", data)
        return data


data_dir = './Datasets/AustensBoxes/'
dataset = CustomDataset(data_dir)
batch_size = 32

num_samples = len(dataset)
num_batches = (num_samples + batch_size - 1) // batch_size

for batch_idx in range(num_batches):
    start_idx = batch_idx * batch_size
    end_idx = min(start_idx + batch_size, num_samples)
    batch_data = [dataset[idx] for idx in range(start_idx, end_idx)]

    # Your training code here
    print("Batch Data Length:", len(batch_data))
