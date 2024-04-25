# пакет shutil, який представляє просунутіший файловий менеджер та вміє працювати з архівами
# Синтаксис методу
# shutil.make_archive(base_name, format, root_dir=None, base_dir=None)
import shutil

# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='my_folder')

# Створення TAR.GZ архіву
shutil.make_archive('example', 'gztar', root_dir='my_folder')

# Функція shutil.unpack_archive() використовується для розпакування архівних файлів
# синтаксис
# shutil.unpack_archive(filename, extract_dir=None, format=None)

import shutil

# Розпакування ZIP-архіву в певну директорію
shutil.unpack_archive('example.zip', 'destination_folder')

# модуль shutil може ще виконувати наступні високорівневі операції для обробки файлової системи

import shutil

# Копіюємо файл
source_file = '/path/to/source/file.txt'
destination_dir = '/path/to/destination'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = '/path/to/source/directory'
destination_dir = '/path/to/destination/directory'
shutil.copytree(source_dir, destination_dir)
