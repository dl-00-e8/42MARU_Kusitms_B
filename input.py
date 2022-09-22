#!python3
# -*- coding:utf-8 -*-

from Module.regex import regex

input_data = '충청남도'

now = regex(input_data)
now.find_loop()
print(now.get_entity_name())
print(now.get_value())
print(now.get_start_idx())
print(now.get_end_idx())
print(now.get_tagged_sentence())