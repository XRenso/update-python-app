import requests
from pathlib import Path
import main
import json
import os
def check_update():
    url = 'https://api.github.com/repos/XRenso/update-python-app/releases/latest'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['tag_name'] != main.program.version:
            assets = data['assets']
            print(assets)
            if assets:  # Проверяем, что список активов не пустой
                asset = max(assets, key=lambda x: x['size'])
                url = asset['browser_download_url']
                file_path = Path(urlparse(url).path).stem
                print(f'Downloading {file_path}...')
                r = requests.get(url, allow_redirects=True)
                with open(file_path, 'wb') as f:
                    f.write(r.content)
                
                # Устанавливаем новую версию
                print('Installing new version...')
                os.system(f'pip install --upgrade {file_path}')

                # Обновляем номер версии в файле
                with open('version.txt', 'w') as f:
                    f.write(data['tag_name'])

            else:
                print("No new versions available.")
    
    return False


def start():
    install = check_update()
    main.run()

start()