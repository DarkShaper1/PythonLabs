import xlrd

table = xlrd.open_workbook('olympicsalltime.xls').sheet_by_index(0)

summer = [[None, 0], [None, 0], [None, 0]]
winter = [[None, 0], [None, 0], [None, 0]]
gold_summer, silver_summer, bronze_summer, gold_winter, silver_winter, bronze_winter = 0, 0, 0, 0, 0, 0
gold_summer_us, silver_summer_us, bronze_summer_us, gold_winter_us, silver_winter_us, bronze_winter_us, total_summer, total_winter = 0, 0, 0, 0, 0, 0, 0, 0
USSR_countries = ('Armenia(ARM)', 'Azerbaijan(AZE)', 'Belarus(BLR)', 'Estonia(EST)', 'Georgia(GEO)', 'Kazakhstan(KAZ)', 'Latvia(LAT)', 'Lithuania(LTU)', 'Moldova(MDA)', 'Russia(RUS)[RUS]', 'Tajikistan(TJK)', 'Ukraine(UKR)', 'Uzbekistan(UZB)')
for i in range(1, table.nrows-1):
    row = table.row_values(i)
    row[0] = str(row[0]).replace('\xa0', '').strip()
    medal_summer = row[2] + row[3] + row[4]
    medal_winter = row[6] + row[7] + row[8]
    if medal_summer > summer[2][1]:
        if medal_summer > summer[1][1]:
            if medal_summer > summer[0][1]:
                summer[2][1] = summer[1][1]
                summer[2][0] = summer[1][0]
                summer[1][1] = summer[0][1]
                summer[1][0] = summer[0][0]
                summer[0][1] = medal_summer
                summer[0][0] = row[0]
            else:
                summer[2][1] = summer[1][1]
                summer[2][0] = summer[1][0]
                summer[1][1] = medal_summer
                summer[1][0] = row[0]
        else:
            summer[2][1] = medal_summer
            summer[2][0] = row[0]
    if medal_winter > winter[2][1]:
        if medal_winter > winter[1][1]:
            if medal_winter > winter[0][1]:
                winter[2][1] = winter[1][1]
                winter[2][0] = winter[1][0]
                winter[1][1] = winter[0][1]
                winter[1][0] = winter[0][0]
                winter[0][1] = medal_winter
                winter[0][0] = row[0]
            else:
                winter[2][1] = winter[1][1]
                winter[2][0] = winter[1][0]
                winter[1][1] = medal_winter
                winter[1][0] = row[0]
        else:
            winter[2][1] = medal_winter
            winter[2][0] = row[0]
    if row[0] == 'Soviet Union(URS)[URS]':
        gold_summer = row[2] / row[1]
        silver_summer = row[3] / row[1]
        bronze_summer = row[4] / row[1]

        gold_winter = row[6] / row[5]
        silver_winter = row[7] / row[5]
        bronze_winter = row[8] / row[5]
    if row[0] in USSR_countries:
        total_summer += row[1]
        total_winter += row[5]
        gold_summer_us += row[2]
        silver_summer_us += row[3]
        bronze_summer_us += row[4]
        gold_winter_us += row[6]
        silver_winter_us += row[7]
        bronze_winter_us += row[8]
print(f'Страны, завоевавшие больше всех медалей на летних играх: {summer[0][0]}({int(summer[0][1])}), {summer[1][0]}({int(summer[1][1])}), {summer[2][0]}({int(summer[2][1])})')
print(f'Страны, завоевавшие больше всех медалей на зимних играх: {winter[0][0]}({int(winter[0][1])}), {winter[1][0]}({int(winter[1][1])}), {winter[2][0]}({int(winter[2][1])})')

print(f'Советский союз за одни летние игры в среднем зарабатывал {round(gold_summer,2)} золотых, {round(silver_summer,2)} серебряных, {round(bronze_summer,2)} бронзовых медалей')
print(f'Советский союз за одни зимние игры в среднем зарабатывал {round(gold_winter,2)} золотых, {round(silver_winter,2)} серебряных, {round(bronze_winter,2)} бронзовых медалей')

print(f'Страны, входившие в Советский союз, за одни летние игры в среднем зарабатывали {round(gold_summer_us/total_summer,2)} золотых, {round(silver_summer_us/total_summer,2)} серебряных, {round(bronze_summer_us/total_summer,2)} бронзовых медалей')
print(f'Страны, входившие в Советский союз, за одни зимние игры в среднем зарабатывали {round(gold_winter_us/total_winter,2)} золотых, {round(silver_winter_us/total_winter,2)} серебряных, {round(bronze_winter_us/total_winter,2)} бронзовых медалей')
