choice = -1
listNewNote = ''

def askForChoice():
    while True:
        try:
            choice = int(input('\nВведите: 1 - если хотите добавить в справочник; 2 - если хотите в него заглянуть:; 3 - для выхода\n'))
            if choice in range(0, 4):
                break
            else: print('Вы ввели неправильно число !!!')
        except:
            print('Неверно указано число!\n')
    return choice


def askForFormat():
    while True:
        format = input('\nВведите: 1 - если хотите использовать справочник в формате .TXT; 2 - если в формате .CSV\n')
        if format == '1' or format == '2':
            return format
        else: 
            print('\nНекорректно указан формат !!!\n')
            continue


def askForNewNote():
    while True:
        listNewNote = input('\nВведите через ЗАПЯТУЮ данные абонента в формате: Фамилия, Имя, Отчество, Телефон:\n').split(',')
        if len(listNewNote) != 4:
            print('Вы ввели некорректное количество данных!!!\n')
            continue
        else:
            return listNewNote