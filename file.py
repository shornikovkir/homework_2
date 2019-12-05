"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""
from collections import Counter

def main():
    with open('c:/projects/homework_2/referat.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        with open('c:/projects/homework_2/referat_2.txt', 'a', encoding='utf-8') as f:
            f.write(f'Кол-во символов: {len(text)}\n')
            f.write(f'Кол-во слов: {len(text.split())}\n\n\n')
            f.write(text.replace('.', '!')) 
    

if __name__ == "__main__":
    main()