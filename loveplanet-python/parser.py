import re
import db

labels   =   {
        'state'     :   u'Отношения:',
        'children'  :   u'Дети:',
        'housing'   :   u'Жилищные условия:',
        'auto'      :   u'Наличие автомобиля:',
        'education' :   u'Образование:',
        'income'    :   u'Доход:',
        'scope'     :   u'Сфера деятельности:',
        'smoke'     :   u'Курение:',
        'alcohol'   :   u'Алкоголь:',
        'foreign'   :   u'Владение иностранными языками:',
        'movies_e'  :   u'Любимые фильмы',
        'education_e':  u'Ваше образование',
        'books_e'   :   u'Любимые книги',
        'hobby_e'   :   u'Любимые занятия',
        'like_e'    :   u'Какие качества вы цените в людях',
        'music_e'   :   u'Любимая музыка',
        }


def check(login):
    res = False
    try:
        res = db.Form.select().where((db.Form.login == login))
    except:
        pass
    return bool(res)


def fillForm (text, url, age):
    ''' sorry for this lame hack :( '''
    f = open('/tmp/parser.tmp', 'w')
    f.write (text)
    f.close()
    f = open ('/tmp/parser.tmp', 'r')
    text = f.read()

    fail = re.findall('Данные о выбранном пользователе не существуют', text)
    if fail:
        print ('fail')
    else:
        weight, height, search_from, search_to  = (0, 0, 0, 0)
        search_who2 = re.findall('Кого я хочу найти.*\n.*\n.*\n.*<li>(.*)</li>', text, re.UNICODE)
        about_me    = re.findall('Свободно о себе.*\n.*\n.*\n.*<li>(.*)</li>', text, re.UNICODE)
        search_who  = re.findall ('Я ищу\n\t*(.*)', text, re.UNICODE)
        search_for  = re.findall ('[0-9]+\n\t*(для.*)', text, re.UNICODE)
        body        = re.findall ('&#44; ([а-яА-Яa-zA-Z]+) телосложение', text, re.UNICODE)
        premium     = re.findall ('svc_icon_sm elite img_clr fr ml3', text, re.UNICODE)

        try:
            search_from = re.findall ('[:space:]*от ([0-9]+)\n', text, re.UNICODE)[0]
            search_to   = re.findall ('[:space:]*до ([0-9]+)\n', text, re.UNICODE)[0]
        except:
            pass
        try:
            weight = re.findall ('([0-9]+) кг', text, re.UNICODE)[0]
        except:
            pass
        try:
            height = re.findall ('([0-9]+) см', text, re.UNICODE)[0]
        except:
            pass

        login = re.findall('/page/(.*)/frl-2', url)[0]
        frm = db.Form(url = url, age = age, login = login, weight = weight, height = height, search_from = search_from, search_to = search_to, search_for = search_for, search_who = search_who, search_who2 = search_who2, about_me = about_me, body = body, premium = premium)
        for field, label in labels.items():
            regex = '<label>'+label+'</label>\n[\s]*<div>(.*)</div>'
            value = re.findall(regex, text, re.UNICODE)
            setattr(frm, field, value )
        frm.save()







