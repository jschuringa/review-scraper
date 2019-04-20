import zipfile
import os
import wget

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'venv/bin')
file_path = path + "/chromedriver_linux64.zip"
if not os.path.isfile(file_path):
    url = 'https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip'
    wget.download(url, out=path)

    zip_ref = zipfile.ZipFile(file_path, 'r')
    zip_ref.extractall(os.path.join(dirname, 'venv/bin'))
    zip_ref.close()
    os.remove(file_path)
    os.chmod(path + '/chromedriver.exe', 0755)
else:
    print("Chrome driver already exists in virtual environment.")
