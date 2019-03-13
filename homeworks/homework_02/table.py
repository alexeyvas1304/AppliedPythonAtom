# -*- coding: utf-8 -*-

import sys

# Ваши импорты

from encoding_identifier import *
from format_identifier import *
from printing import *
import os.path

if __name__ == '__main__':
    filename = sys.argv[1]
    if os.path.isfile(filename) is False:
        print("Файл не валиден")
    elif define_encoding(filename) is None:
        print("Формат не валиден")
    elif define_format(filename, define_encoding(filename)) is None:
        print("Формат не валиден")
    else:
        encode = define_encoding(filename)
        formats = define_format(filename, encode)
        print_table(filename, encode, formats)
