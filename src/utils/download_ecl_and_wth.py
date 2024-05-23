import gdown

# Google Drive file IDs
ECL_ID = '1tK3Ub3Gu5mvXa5U4Y4jGO_r5YUbW5u93'
WTH_ID = '1to-HCS5_nHb_fxxRmyveES7ABplFyoYV'

# URLs for the datasets
ECL_URL = f'https://drive.google.com/uc?export=download&id={ECL_ID}'
WTH_URL = f'https://drive.google.com/uc?export=download&id={WTH_ID}'

# Output filenames
ECL_FILE = 'ECL.csv'
WTH_FILE = 'WTH.csv'

# Download the datasets
print("Downloading ECL dataset...")
gdown.download(ECL_URL, ECL_FILE, quiet=False)

print("Downloading WTH dataset...")
gdown.download(WTH_URL, WTH_FILE, quiet=False)

print("Download completed!")
