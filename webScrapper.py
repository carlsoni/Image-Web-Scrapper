import os
import requests
from bs4 import BeautifulSoup
import urllib.request

def download_images(url, folder_path):
   
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    images = soup.find_all('img')

    for i, img in enumerate(images):
        src = img.get('src')
        if not src.startswith(('http:', 'https:')):
            src = urllib.parse.urljoin(url, src)
        try:
            with open(os.path.join(folder_path, f'image_{i}.jpg'), 'wb') as file:
                img_data = requests.get(src).content
                file.write(img_data)
                print(f"Downloaded {src}")
        except Exception as e:
            print(f"Could not download {src}. Reason: {e}")

url = 'https://arboretum.harvard.edu/plants/image-search/'
folder_path = '/Users/ianexclam/Desktop/Capstone'
download_images(url, folder_path)
