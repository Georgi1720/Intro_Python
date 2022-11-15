import os
from os.path import exists
from Creating_head import creating_txt
from Creating_head import creating_csv

def open_txt():
    path = 'txt_PhoneBook.txt'
    valid = exists(path)
    if valid != True:
        creating_txt()
    
    osCommandString = f'notepad.exe {path}'
    os.system(osCommandString)


def open_csv():
    path = 'csv_PhoneBook.csv'
    valid = exists(path)
    if valid != True:
        creating_csv()
    
    osCommandString = f'notepad.exe {path}'
    os.system(osCommandString)
