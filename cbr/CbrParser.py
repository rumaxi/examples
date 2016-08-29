import re
import requests

SOURCE  = 'http://www.cbr.ru/mcirabis/PluginInterface/GetBicCatalog.aspx'
PATH    = 'http://www.cbr.ru/mcirabis/BIK/'

biclist = requests.get(SOURCE).text

for filename in re.findall('file="([a-zA-Z0-9_]+2016.zip)"', biclist):
        with open(filename, 'wb') as f:
            url = PATH + filename
            data = requests.get(url, stream = True).raw.read()
            f.write(data)
            print (filename+' ok')
