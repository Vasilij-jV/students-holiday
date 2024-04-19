import csv


def write_holiday_cities(first_letter):
    have_visited = []
    want_to_visit = []
    no_one_has_been_to = []
    with open('travel-notes.csv', mode='r', newline='', encoding='utf-8') as tr:
        reader = csv.reader(tr)
        # Заполняю два списка из трёх
        for row in reader:
            if row[0].startswith(first_letter):
                have_visited += row[1].split(';')
                want_to_visit += row[2].split(';')
                no_one_has_been_to += row[2].split(';')
        # Сортирую списки по алфавиту
        have_visited.sort()
        want_to_visit.sort()
        no_one_has_been_to.sort()

    # Форматирование строк
    have_visited.insert(0, 'Посетили:')
    for elem in range(len(have_visited)):
        if elem == 0:
            continue
        have_visited[elem] = have_visited[elem][:] + ','

    want_to_visit.insert(0, 'Хотят посетить:')
    for elem in range(len(want_to_visit)):
        if elem == 0:
            continue
        want_to_visit[elem] = want_to_visit[elem][:] + ','

    no_one_has_been_to.insert(0, 'Никогда не были:')
    for elem in range(len(no_one_has_been_to)):
        if elem == 0:
            continue
        no_one_has_been_to[elem] = no_one_has_been_to[elem][:] + ','

    with open('holiday.csv', mode='w', newline='', encoding='utf-8') as hl:
        writer = csv.writer(hl, delimiter=' ', quotechar=' ', escapechar=' ', quoting=csv.QUOTE_NONE)
        writer.writerow(have_visited)
        writer.writerow(want_to_visit)
        writer.writerow(no_one_has_been_to)
        writer.writerow([f'Следующим городом будет: {want_to_visit[1]}'])

    print(have_visited)


write_holiday_cities('L')
