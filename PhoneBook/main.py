from Writing import txt_write
from Writing import csv_write
from Reading import open_csv
from Reading import open_txt

def main_run():
    total_command = input('Введите "W", чтобы добавить контакт. Или "R", чтобы постотреть телефонную книгу: ')

    if total_command == 'W':
        command_write = input('Введите формат записи (.txt / .csv): ')
        if command_write == 'txt':
            txt_write()
        elif command_write == 'csv':
            csv_write()

    elif total_command == 'R':
        command_read = input('Введите формат просмотра (.txt / .csv): ')
        if command_read == 'txt':
            open_txt()
        elif command_read == 'csv':
            open_csv()
    else: 
        print('Неверная команда')

main_run()
