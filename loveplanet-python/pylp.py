#!/usr/bin/python3
import requests
import parser
import sys
import re

base_url = 'http://loveplanet.ru'
auth_url  = 'http://loveplanet.ru/a-logon/'
auth_data = {
 'a'         :   'logon',
 'login'     :   '<login>',
 'password'  :   '<password>',
}
search_url = 'http://loveplanet.ru/a-search/'
search_query = 'd-1/foto-1/pol-1/spol-2/bage-{bage}/tage-{tage}/geo-3159%2C4312%2C4400/country-3159/region-4312/city-4400/p-{page}'
page_regex = r'class="buser_usname".*2/'
headers = {
 'User-Agent': 'Mozilla/5.0 (compatible; Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
}


r = requests.post ( auth_url, data = auth_data, headers = headers, allow_redirects=False )
cookies = r.cookies


stats = {'total':0,'passed':0, 'visited':0}


for age in range (20,40):
    for page in range(150):
        q = search_query.format(bage=age, tage=age, page=page)
        url = search_url+ q
        r = requests.get ( url, headers = headers )
        pages = re.findall (page_regex, r.text)
        for page in pages:
            stats['total']+=1
            page_url = page.split('"')[3]
            login = re.findall('/page/(.*)/frl-2', page_url)[0]
            if parser.check(login):
                stats['passed']+=1
            else:
                stats['visited']+=1
            if age not in stats.keys():
                stats[age]=0
                stats[age]+=1
            url = base_url + page_url
            r = requests.get ( url, headers = headers, cookies = cookies )
            r = requests.get ( url, headers = headers, cookies = cookies )
            print (url)
                parser.fillForm (r.text, page_url, age)
        print (stats)


