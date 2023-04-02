from datetime import datetime as dt


def main(table):
    result = list(map(list, zip(*table)))
    unique_rows = []

    for row in result:
        if row not in unique_rows:
            unique_rows.append(row)

    result = unique_rows

    for i in range(len(result[0])):
        if result[0][i] is not None:
            result[0][i] = result[0][i].split()[0]

        if result[1][i] is not None:
            result[1][i] = 'true' if result[1][i] == 'Да' else 'false'

        if result[2][i] is not None:
            result[2][i] = result[2][i].replace('@', '[at]')

        if result[3][i] is not None:
            date_obj = dt.strptime(result[3][i], '%d-%m-%Y')
            result[3][i] = date_obj.strftime('%Y.%m.%d')

    return result


print(main([['Ширяк Альберт', 'Да', 'al_bert76@yandex.ru', 'Да', '24-06-2002'], ['Сомак Рустам', 'Да', 'rustam65@yandex.ru', 'Да', '02-04-2000'], ['Монев Семен', 'Да', 'monev72@mail.ru', 'Да', '15-09-2002']]))
