from lxml import etree
import requests

number_of_bus = input('Введите номер автобуса: ')
htmlreq = requests.get(f'https://www.ot76.ru/mob/getroutestr.php?vt=1&nmar={number_of_bus}')

doc1 = etree.HTML(htmlreq.text)
xp2 = etree.XPath('/html/body/table/tr/td[2] | /html/body/table/tr/td[3]')
xp3 = etree.XPath('/html/body/table/tr/td/a/@href')
step, bort, point, name = 0, 0, 0, 0
buses = []

for i in xp2(doc1):
    for item in i.iter():
        if item.tag == 'td' and item.text is not None:
            if item.text.isdigit():
                bort = item.text
            else:
                buses.append([bort, item.text])

bus = 0
for i in xp3(doc1):
    htmlreq = requests.get(f'https://www.ot76.ru/mob/{i}')
    doc2 = etree.HTML(htmlreq.text)
    xp4 = etree.XPath('/html/body/table/tr[4]/td')
    step = 0
    for g in xp4(doc2):
        for item in g.iter():
            if item.tag == 'td' and item.text is not None:
                step += 1
                if step == 1:
                    name = item.text
                if step == 2:
                    buses[bus].append([name, item.text])
                    step = 0
    else:
        bus += 1
if len(buses) > 0:
    print(f'----------------------------------- Расписание для {number_of_bus} автобуса -----------------------------------')
    for i in buses:
        try:
            print(f'Борт номер {i[0]} сейчас находтся на остановке {i[1]}. Следующая остановка {i[2][0]} в {i[2][1]}')
        except IndexError:
            print(f'Ошибка в расписании: Борт номер {i[0]} (Расписания нет на сайте)')
    print(f'-------------------------------------------------------------------------------------------------')
else:
    print('Такого автобуса нет на карте')

