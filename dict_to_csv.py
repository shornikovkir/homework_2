"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""
import csv

personal = [
            {'name':'Маша', 'age':25, 'job':'Scientist'}, 
            {'name':'Вася', 'age':8, 'job':'Programmer'}, 
            {'name':'Эдуард', 'age':48, 'job':'Big boss'},
]

def main():
    with open('users.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for pers in personal:
            writer.writerow(pers)

if __name__ == "__main__":
    main()


