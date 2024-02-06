import os
import requests
from bs4 import BeautifulSoup
import urllib.request

def download_images(url, folder_path):
    # Make a request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Create a folder for the images if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Find all image tags in the HTML
    images = soup.find_all('img')

    for i, img in enumerate(images):
        # Get the source attribute of each image
        src = img.get('src')
        # Complete the src with the base url if needed
        if not src.startswith(('http:', 'https:')):
            src = urllib.parse.urljoin(url, src)
        # Get the content of the image
        try:
            with open(os.path.join(folder_path, f'image_{i}.jpg'), 'wb') as file:
                img_data = requests.get(src).content
                file.write(img_data)
                print(f"Downloaded {src}")
        except Exception as e:
            print(f"Could not download {src}. Reason: {e}")

# Example usage
url = 'https://arboretum.harvard.edu/plants/image-search/'
folder_path = '/Users/ianexclam/Desktop/Capstone'
download_images(url, folder_path)
