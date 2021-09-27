"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить
кодировку файла по умолчанию. Принудительно открыть файл в
формате Unicode и вывести его содержимое
"""

LINES = ["сетевое программирование", "сокет", "декоратор"]

with open('test_file.txt', 'w') as f:  # кодировка файла по умолчанию
    for line in LINES:
        f.write(line)
        f.write('\n')
    print(f)  # <_io.TextIOWrapper name='test_file.txt' mode='w' encoding='cp1251'>

with open('test_file.txt', 'r', encoding='utf-8', errors='replace') as f:
    print(f.read())
