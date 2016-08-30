import requests as r
from lxml.html import parse
import db
import re



paginator_regex     = 'name="pager"'
item_links_regex    = 'listing-item__link link__control i-bem" href="//(auto.ru/cars/used/sale/[a-zA-Z0-9\-]*/)' 
mileage_regex   = '>([0-9 ]*) км'
owner_regex     = '([0-9]*) владе'
price_regex     = 'rur">([0-9 ]*)&#160'

#model='https://moscow.auto.ru/cars/renault/megane/all/'
#model='https://moscow.auto.ru/cars/audi/q7/all/'
#model='https://moscow.auto.ru/cars/volkswagen/touareg/all/'
#model='https://moscow.auto.ru/cars/renault/logan/all/'
model='https://moscow.auto.ru/cars/bmw/5er/all/'



for year in range (2005,2015):
    print (year)
    yearlink = model+"?listing=listing&sort_offers=price-ASC&top_days=off&currency=RUR&output_type=list&image=true&is_clear=false&beaten=1&customs_state=1&geo_id%5B%5D=213&page_num_offers=1&year_from="+str(year)+"&year_to="+str(year)
    page = r.get(yearlink)
    pages=len(re.findall (paginator_regex, page.text))
    print (pages)
    if pages == 0:
        pages = 1
    for pagen in range(0,pages):
        cpage = pagen+1
        pagelink = model+"?listing=listing&sort_offers=price-ASC&top_days=off&currency=RUR&output_type=list&image=true&is_clear=false&beaten=1&customs_state=1&geo_id%5B%5D=213&year_from="+str(year)+"&year_to="+str(year)+"&page_num_offers="+str(cpage)
        catpage = r.get(pagelink)
        items = re.findall(item_links_regex, catpage.text)
        for item in items:
            itempage = r.get ('https://'+item)
            itempage.encoding='utf-8'
            try:
                mileage = re.findall(mileage_regex, itempage.text, re.UNICODE)[0].replace(" ", "")
            except:
                pass

            try:
                price   = re.findall(price_regex, itempage.text, re.UNICODE)[0].replace(" ", "")
            except:
                pass
            try:
                owner   = re.findall(owner_regex, itempage.text, re.UNICODE)[0]
            except:
                pass
            with open('test2','w') as f:
                f.write (itempage.text)
            print (item)
            print (mileage)
            print (price)
            db.Auto.create(price=price, mileage = mileage, year = year)
