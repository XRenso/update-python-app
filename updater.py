import requests
from pathlib import Path
import main
import json
from urllib.parse import urlparse
import sys
import os
def check_update():
    url = 'https://api.github.com/repos/XRenso/update-python-app/releases/latest'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['tag_name'] != main.program.version:
            assets = data['assets']
            if assets:  # Проверяем, что список активов не пустой
                asset = max(assets, key=lambda x: x['size'])
                url = asset['browser_download_url']
                file_path = Path(urlparse(url).path).stem +  Path(urlparse(url).path).suffix
                print(f'Downloading {file_path}...')
                r = requests.get(url, allow_redirects=True)
                with open(file_path, 'w+') as f:
                    f.write(r.content)
                return True
    
    return False


def start():
    install = check_update()
    if install:
        input('Enter for restart')
        os.execv(os.getcwd()+'main.exe', ['python'] + sys.argv)
    else:
        os.execv(os.getcwd()+'main.exe',  ['python'] + sys.argv)
start()