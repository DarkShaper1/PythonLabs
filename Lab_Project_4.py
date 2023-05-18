from lxml import etree

doc = etree.parse('movies.xml')
node = doc.getroot()

years = {}
actors = {}
actors_years = {}
year = 0
for item in node.iter():
    # print(item.tag)
    if item.tag == 'year' and item.text.isdigit():
        year = int(item.text)
        if item.text in years:
            years[item.text] += 1
        elif item.text:
            years[item.text] = 1
    elif item.tag == 'actor':
        if item.text in actors:
            actors[item.text] += 1
        else:
            actors[item.text] = 1
        if item.text in actors_years:
            if actors_years[item.text][0] > year:
                actors_years[item.text][0] = year
            if actors_years[item.text][1] < year:
                actors_years[item.text][1] = year
        else:
            actors_years[item.text] = [year, year]

years_list = list(years.items())
actors_list = list(actors.items())
actors_years_list = list(actors_years.items())

years_list.sort(key=lambda x: x[1], reverse=True)
actors_list.sort(key=lambda x: x[1], reverse=True)
actors_years_list.sort(key=lambda x: x[1][1]-x[1][0], reverse=True)

print(f'Три года, в которые выпускалось наибольшее количество картин: {years_list[0][0]}({years_list[0][1]} картин), {years_list[1][0]}({years_list[1][1]} картин), {years_list[2][0]}({years_list[2][1]} картин)')
print(f'Три года, в которые выпускалось наименьшее количество картин: {years_list[-1][0]}({years_list[-1][1]} картин), {years_list[-2][0]}({years_list[-2][1]} картин), {years_list[-3][0]}({years_list[-3][1]} картин)')

print(f'{actors_list[0][0].replace(",", "")} играл в наибольшем количестве фильмов ({actors_list[0][1]})')

print(f'Самая длинная кинематографическая карьера у {actors_years_list[0][0].replace(",", "")}({actors_years_list[0][1][1] - actors_years_list[0][1][0]} лет)')
