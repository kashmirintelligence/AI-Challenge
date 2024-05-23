import os
import requests

# List of CSV files to download
csv_files = [
    "ETTh1.csv",
    "ETTh2.csv",
    "ETTm1.csv",
    "ETTm2.csv"
]

# Base URL for the GitHub repository
base_url = "https://raw.githubusercontent.com/zhouhaoyi/ETDataset/main/ETT-small/"

# Directory to save the downloaded files
save_dir = "ETT-small"
os.makedirs(save_dir, exist_ok=True)

def download_csv(file_name):
    """
    Download a CSV file from the GitHub repository and save it locally.
    
    :param file_name: str, Name of the CSV file to download.
    """
    url = base_url + file_name
    response = requests.get(url)
    
    if response.status_code == 200:
        file_path = os.path.join(save_dir, file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")

if __name__ == "__main__":
    for csv_file in csv_files:
        download_csv(csv_file)
