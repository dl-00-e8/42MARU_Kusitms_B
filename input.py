#!python3
# -*- coding:utf-8 -*-

from Module.regex import regex

input_data = '오늘은 108도야!, 내일은 100도래'

now = regex(input_data)
now.find_regex()
print(now.get_entity_name())
print(now.get_value())
print(now.get_start_idx())
print(now.get_end_idx())
print(now.get_tagged_sentence())