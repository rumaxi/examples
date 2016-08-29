import requests
from lxml.html import parse

SOURCE  = 'http://www.cbr.ru/mcirabis/?Prtid=bic'
PATH    = 'http://www.cbr.ru/mcirabis/BIK/'

dom = parse(SOURCE).getroot()

# <p class="file ZIP small_icon"><a href="/mcirabis/BIK/bik_dc_2757_02022016.zip"><i class="icon"></     i>bik_dc_2757_02022016.zip</a </p>

for tag in dom.cssselect('.file.ZIP.small_icon a'):
    filename = tag.text_content()
    url = PATH + filename
    data = requests.get(url, stream = True).raw.read()
    f = open(filename, 'wb')
    f.write(data)
    print (filename+' ok')

