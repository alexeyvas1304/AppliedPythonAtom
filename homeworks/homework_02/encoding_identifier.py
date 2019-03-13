# -*- coding: utf-8 -*-


def is_utf8(f_name):
    try:
        with open(f_name, encoding='utf8') as f:
            f.read()
    except Exception:
        return False
    else:
        return True


def is_cp1251(f_name):
    try:
        with open(f_name, encoding='cp1251') as f:

            f.read()
    except Exception:
        return False
    else:
        return True


def is_utf16(f_name):
    try:
        with open(f_name, encoding='utf16') as f:
            f.read()
    except Exception:
        return False
    else:
        return True


def define_encoding(f_name):
    if is_utf8(f_name) is True:
        return 'utf8'
    elif is_utf16(f_name):
        return 'utf16'
    elif is_cp1251(f_name):
        return 'cp1251'
    else:
        return None

# __all__ = ["define_encoding"]
