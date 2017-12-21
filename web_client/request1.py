import requests

params = {'firstname':'hu','lastname':'baba'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php',data = params)
print(r.text)