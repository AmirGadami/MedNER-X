import os

def read_dataset(data_path, filenames):

    """
Reads multiple dataset files and combines them into a single list.

Args:
    data_path (str): Path to the data directory.
    filenames (list): List of dataset filenames.

Returns:
    list: Combined list of all dataset lines.
"""

    combined_data = []
    for file in filenames:

        with open(os.path.join(data_path,file),'r',encoding='utf-8') as f:
            combined_data.extend(f.readlines())
    return combined_data









if __name__ == "__main__":
    from config import FILENAMES, RAW_DATA_PATH

    data = read_dataset(RAW_DATA_PATH,FILENAMES)
    print(data[10])