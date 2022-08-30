# python downloader version 1.0
from fileinput import filename
import requests
print("===========================")
print("=                         =")
print("=   PyDownloader V1.0     =")
print("=                         =")
print("===========================")
DOWNLOAD_URL = input("Paste the URL here: ")

req = requests.get(DOWNLOAD_URL)
filename = req.url[DOWNLOAD_URL.rfind('/')+1:]

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

def download_file(url, filename=''):
    try:
        if filename:
            pass
        else:
            filename = req.url[DOWNLOAD_URL.rfind('/')+1:]
        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None

