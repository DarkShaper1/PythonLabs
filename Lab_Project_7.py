import csv
import requests
from lxml import etree


def jaccard(string1, string2):
    string3 = [string1[step - 1:step + 1] for step in range(1, len(string1))]
    string4 = [string2[step - 1:step + 1] for step in range(1, len(string2))]
    intersection = len(list(set(string3).intersection(string4)))
    union = (len(set(string3)) + len(set(string4))) - intersection
    return float(intersection) / union


passengers = []
with open('titanic_passengers.csv', 'r') as csvfile:
    file = csv.reader(csvfile, delimiter=',', quotechar='|')
    for line in file:
        passengers.append(line)
del passengers[0]
url = 'https://en.wikipedia.org/wiki/Passengers_of_the_Titanic'
req = requests.get(url)
with open("wikipedia_copy.html", "w", encoding="utf-8") as file:
    file.write(req.text)

passengers_wiki = []
passengers_text = []
doc1 = etree.HTML(req.text)
xp = etree.XPath('/html/body/div[3]/div[3]/div[5]/div[1]/table/tbody/tr/td[1]')
for i in xp(doc1):
    for item in i.iter():
        if (item.tag == 'td' or item.tag == 'a') and item.text is not None:
            if item.text[0] != '[':
                pas = item.text.replace('\n', '').strip()
                passengers_wiki.append(pas)
for i in range(len(passengers)):
    first_name = passengers[i][4].strip()
    last_name = passengers[i][3].strip()
    passengers_text.append(f'{last_name}, {first_name}')

passengers_text = list(set(passengers_text))
passengers_wiki = list(set(passengers_wiki))
count = 0
percent_of_similarity = 0.47  # Изменение значения меры Жакарда
for i in passengers_wiki:
    flag = False
    for g in passengers_text:
        if jaccard(i, g) > percent_of_similarity:
            flag = True
            break
    if not flag:
        print(f'{i} есть в Википедии, но нет в файле')
        count += 1
for i in passengers_text:
    flag = False
    for g in passengers_wiki:
        if jaccard(i, g) > percent_of_similarity:
            flag = True
            break
    if not flag:
        print(f'{i} есть в файле, но нет в википедии')
        count += 1
print(f'{count} расхождений по мере Жакарда')
print(f'{len(passengers_wiki) - len(passengers_text)} расхождений должно быть примерно')
