from operator import itemgetter


class Musician:
    def __init__(self, id, fio, sal, dep_id):
        self.id = id

    self.fio = fio
    self.sal = sal
    self.dep_id = dep_id


class Orchestra:
    def __init__(self, id, name):
        self.id = id

    self.name = name


# Оркесты
orchestras = [
    Orchestra(1, 'Лондонский симфонический'),
    Orchestra(2, 'Большой симфонический'),
    Orchestra(3, 'Бостонский симфонический'),
    Orchestra(4, 'Российский национальный'),
    Orchestra(5, 'Чикагский симфонический'),
    Orchestra(6, 'Берлинский филармонический'),
]
# Музыканы
musicians = [
    Musician(1, 'Лифановский', 50000, 1),
    Musician(2, 'Чайковский', 75000, 2),
    Musician(3, 'Рахманинов', 60000, 3),
    Musician(4, 'Шостакович', 45000, 3),
    Musician(5, 'Ивашкин', 100000, 5),
    Musician(6, 'Рябинин', 45000, 5),
    Musician(7, 'Козолупов', 120000, 1),
    Musician(8, 'Лебедев', 80000, 6),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(e.fio, e.sal, d.name)
                   for d in orchestras
                   for e in musicians
                   if e.dep_id == d.id]
    print('Задание 1: ')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание 2')
    res_12_unsorted = []

    # Перебираем все оркестры
    for d in orchestras:
    # Список музыкантов оркестра
    d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
    # Если оркестр не пустой
    if len(d_emps) > 0:
    # Зарплаты музыкантов оркестра
    d_sals = [sal for _, sal, _ in d_emps]
    # Суммарная зарплата музыкантор отдела
    d_sals_sum = sum(d_sals)
    res_12_unsorted.append((d.name, d_sals_sum))
    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


if __name__ == '__main__':
    main()
    