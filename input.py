#!python3
# -*- coding:utf-8 -*-

from Module.regex import regex

input_data = '시속 100km/h의 정상수'

now = regex(input_data)
now.find_loop()
print(now.get_entity_name())
print(now.get_value())
print(now.get_start_idx())
print(now.get_end_idx())
print(now.get_tagged_sentence())