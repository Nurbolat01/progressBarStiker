#     A progress bar with funny stikers that changes every time 
#     when progress achive a number of condition


import requests

def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    chunk_size = 1024  # You can adjust the chunk size as needed
    downloaded = 0
    stickers = ["😡", "😐", "😊", "😄"]
    current_sticker = 0
    with open(filename, 'wb') as file:
        for data in response.iter_content(chunk_size=chunk_size):
            file.write(data)
            downloaded += len(data)
            progress = (downloaded / total_size) * 100
            if progress >= 75:
                print(f"\rDownloading... [{stickers[3]}|{int(progress)}%]", end='', flush=True)
            elif progress >= 50:
                print(f"\rDownloading... [{stickers[2]}|{int(progress)}%]", end='', flush=True)
            elif progress >= 25:
                print(f"\rDownloading... [{stickers[1]}|{int(progress)}%]", end='', flush=True)
            else:
                print(f"\rDownloading... [{stickers[0]}|{int(progress)}%]", end='', flush=True)

    print("\nDownload complete.")

url = 'https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt'  # Replace with the actual URL of the file you're downloading
filename = 'rockyou.zip'  # Replace with the desired filename

download_file(url, filename)
