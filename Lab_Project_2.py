first_class = 0
second_class = 0
third_class = 0
survived_first_class = 0
survived_second_class = 0
survived_third_class = 0
male_survived = 0
female_survived = 0
male_survived_first_class = 0
male_survived_second_class = 0
male_survived_third_class = 0
female_survived_first_class = 0
female_survived_second_class = 0
female_survived_third_class = 0
died = 0
survived = 0
age_passengers = []
step = 0
max_price_first_class = 0
avg_price_first_class = 0
min_price_first_class = 10000
max_price_second_class = 0
avg_price_second_class = 0
min_price_second_class = 10000
max_price_third_class = 0
avg_price_third_class = 0
min_price_third_class = 10000
with open('titanic_passengers.csv', encoding='utf-8') as f:
    for line in f:
        data = line.replace('\n', '').split(',')

        if data[2] == '1':
            first_class += 1
            if float(data[10]) > max_price_first_class:
                max_price_first_class = float(data[10])
            if float(data[10]) < min_price_first_class:
                min_price_first_class = float(data[10])
            avg_price_first_class += float(data[10])
            if data[1] == '1':
                survived_first_class += 1
                if data[5] == 'male':
                    male_survived_first_class += 1
                elif data[5] == 'female':
                    female_survived_first_class += 1

        elif data[2] == '2':
            second_class += 1
            if float(data[10]) > max_price_second_class:
                max_price_second_class = float(data[10])
            if float(data[10]) < min_price_second_class:
                min_price_second_class = float(data[10])
            avg_price_second_class += float(data[10])
            if data[1] == '1':
                survived_second_class += 1
                if data[5] == 'male':
                    male_survived_second_class += 1
                elif data[5] == 'female':
                    female_survived_second_class += 1

        elif data[2] == '3':
            third_class += 1
            if float(data[10]) > max_price_third_class:
                max_price_third_class = float(data[10])
            if float(data[10]) < min_price_third_class:
                min_price_third_class = float(data[10])
            avg_price_third_class += float(data[10])
            if data[1] == '1':
                survived_third_class += 1
                if data[5] == 'male':
                    male_survived_third_class += 1
                elif data[5] == 'female':
                    female_survived_third_class += 1

        if data[1] == '0':
            died += 1
        elif data[1] == '1':
            survived += 1
            if data[5] == 'male':
                male_survived += 1
            elif data[5] == 'female':
                female_survived += 1
        if not data[6].isalpha() and data[6] is not None and data[1] == '1' and data[6] != '':
            age_passengers.append([])
            age_passengers[step].append(f'{data[3]} {data[4]}')
            age_passengers[step].append(data[6])
            step += 1

print(f'В первом классе летело {first_class} человек')
print(f'Во втором классе летело {second_class} человек')
print(f'В третьем классе летело {third_class} человек')
print()
print(f'Выжило {survived} человек')
print(f'Утонуло {died} человек')
print()
print(f'В первом классе выжило {survived_first_class} человек')
print(f'Во втором классе выжило {survived_second_class} человек')
print(f'В третьем классе выжило {survived_third_class} человек')
print()
if male_survived > female_survived:
    print('Мужчин выжило больше')
else:
    print('Женщин выжило больше')
print()
print(f'В первом классе выжило {male_survived_first_class} мужчин и {female_survived_first_class} женщин')
print(f'Во втором классе выжило {male_survived_second_class} мужчин и {female_survived_second_class} женщин')
print(f'В третьем классе выжило {male_survived_third_class} мужчин и {female_survived_third_class} женщин')
age_passengers.sort(key=lambda x: float(x[1]), reverse=True)
old_persons = ', '.join(f'{age_passengers[i][0]}({age_passengers[i][1]})' for i in range(5))
young_persons = ', '.join(f'{age_passengers[i][0]}({age_passengers[i][1]})' for i in range(len(age_passengers)-1, len(age_passengers)-6, -1))
print(f'Пять самых старших выживших: {old_persons}')
print(f'Пять самых молодых выживших: {young_persons}')
print()
print(f'Максимальная цена в первом классе: {max_price_first_class}')
print(f'Минимальная цена в первом классе: {min_price_first_class}')
print(f'Средняя цена в первом классе: {avg_price_first_class/first_class}')

print(f'Максимальная цена во втором классе: {max_price_second_class}')
print(f'Минимальная цена во втором классе: {min_price_second_class}')
print(f'Средняя цена во втором классе: {avg_price_second_class/second_class}')

print(f'Максимальная цена в третьем классе: {max_price_third_class}')
print(f'Минимальная цена в третьем классе: {min_price_third_class}')
print(f'Средняя цена в третьем классе: {avg_price_third_class/third_class}')
