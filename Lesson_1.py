"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в
строковом формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат
Unicode и также проверить тип и содержимое переменных.
"""

if __name__ == '__main__':

    WORLDS = {
        'разработка': '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
        'сокет': '\u0441\u043e\u043a\u0435\u0442',
        'декоратор': '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440',
    }

    for string_rep, unicode_rep in WORLDS.items():
        print(f'строковый формат слова: "{string_rep}" имеет тип: {type(string_rep)}')
        print(f'формат Unicode слова: "{unicode_rep}" имеет тип: {type(unicode_rep)}')

"""
2. Каждое из слов «class», «function», «method» записать в байтовом
типе без преобразования в последовательность кодов (не
используя методы encode и decode) и определить тип, содержимое
 и длину соответствующих переменных.
"""
if __name__ == '__main__':
    WORLDS = ['class', 'function', 'method']
    worlds_b = [bytes(world, 'ASCII') for world in WORLDS]
    for world_b in worlds_b:
        print(f'тип: {type(world_b)}, содержимое: {world_b}, длина: {len(world_b)}')

"""
3. Определить, какие из слов
«attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
"""


def is_write_in_bytes(_word):
    try:
        bytes(_word, 'ASCII')
    except UnicodeEncodeError:
        print(f'слово: "{_word}" не возможно записать в байтовом типе')


if __name__ == '__main__':
    WORLDS = ['attribute', 'класс', 'функция', 'type']
    for world in WORLDS:
        is_write_in_bytes(world)

"""
4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить обратное преобразование
(используя методы encode и decode).
"""


def type_test(*args):
    for item in args:
        print(item, type(item))


if __name__ == "__main__":
    WORLDS = ['разработка', 'администрирование', 'protocol', 'standard']

    enc_worlds = [world.encode('utf-8') for world in WORLDS]
    print('\nрезультат преобразования в байтовое представление: ')
    type_test(*enc_worlds)

    dec_worlds = [world.decode('utf-8') for world in enc_worlds]
    print('\nрезультат преобразования в стороковое представление: ')
    type_test(*dec_worlds)

"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице.
"""
import subprocess

if __name__ == "__main__":
    SITES = ['yandex.ru', 'youtube.com']
    for site in SITES:
        print(f'\nпинг веб-ресурса: {site}')
        args = ['ping', site]
        subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in subproc_ping.stdout:
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))

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
