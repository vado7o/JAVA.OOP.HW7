import operate_module
import view
import operate_module as wr
import os


def startProgram():
    os.system('cls')
    while True:
        choice = view.askForChoice()
        if choice == 1:
            if view.askForFormat() == '1':
                wr.operate('phonebook.txt', 'write')
            else:
                wr.operate('phonebook.csv', 'write')
            print('\nИнформация успешно записана в книгу !!!\n')

        elif choice == 2:
            if view.askForFormat() == '1':
                operate_module.read('phonebook.txt')
            else:
                operate_module.read('phonebook.csv')

        else:
            break
