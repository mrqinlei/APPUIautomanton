#-*- coding: utf-8 -*-

import string


def del_symbol(str_temp):
    return str_temp.translate(str.maketrans('', '', string.punctuation))

def del_str(str_temp, del_str):
    return str_temp.translate(str.maketrans('','', del_str))