import requests
from pathlib import Path
import main
import os
def check_update():
    url = 'https://github.com/XRenso/update-python-app/releases/latest'
    response = requests.get(url)
    data = response.json()
    if data['tag_name'] != main.program.version:
        assets = data['assets']
        asset = max(assets,key=lambda x: x['size'])
        url = asset['browser_download_url']
        file_path = Path(urlparse(url).path).stem
        print(f'Загружаем {file_path}...')
        r = requests.get(url, allow_redirects=True)
        with open(file_path, 'wb') as f:
            f.write(r.content)
        
        # Устанавливаем новую версию
        print('Скачиваем новую версию')
        os.system(f'pip install --upgrade {file_path}')


        print('Програма обновленка')
        return True
    else:
        return False


def start():
    install = check_update()
    main.run()