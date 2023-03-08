import view

def operate(file, operation):
    with open(file, 'r+', encoding = 'utf-8') as file:
        string = file.read()

        if operation == 'write':
            new_str = ','.join(list(map(lambda x: x.strip(), view.askForNewNote())))
            file.writelines(f'\n{new_str}')

        elif operation == 'read':
             return string


def read(file):
    line = "+---------------------------------------------------------------------------------------------------------------------------+"
    print(line)
    print("|           Фамилия            |             Имя              |            Отчество          |           Телефон            |")
    print(line)
    with open(file, encoding="utf8") as f:
        for i in f.readlines():
            array = i.split(',')
            print("|", end='')
            for str in array:
                if "\n" in str: str = str.replace("\n", "")
                print(str + " " * (30 - len(str)) +  "|", end='')
            print("\n"+line)
