import requests
from pathlib import Path
import json
from urllib.parse import urlparse
import sys
import os

def check_version_txt():

    if not os.path.exists(os.getcwd()+'version.txt'):
        with open('version.txt','w') as f:
            f.write('v1.0.0')

def check_update():
    url = 'https://api.github.com/repos/XRenso/update-python-app/releases/latest'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        if data['tag_name'] != open('version.txt','r').readline().strip():
            assets = data['assets']
            if assets:  # Проверяем, что список активов не пустой
                asset = max(assets, key=lambda x: x['size'])
                url = asset['browser_download_url']
                file_path = Path(urlparse(url).path).stem +  Path(urlparse(url).path).suffix
                print(f'Downloading {file_path}...')
                r = requests.get(url, allow_redirects=True)
                with open(file_path, 'wb+') as f:
                    f.write(r.content)
                with open('version.txt', 'w') as f:
                    f.write(data['tag_name'])
                return True
    
    return False


def start():
    check_version_txt()
    check_update()
start()