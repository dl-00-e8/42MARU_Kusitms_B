#!python3
# -*- coding:utf-8 -*-

from Module.regex import regex

input_data = '2022년 9월 22일 사수자리 운세 알려줘'

now = regex(input_data)
now.find_loop()
'''
# pytest 확인용 메소드
print(now.get_entity_name())
print(now.get_value())
print(now.get_start_idx())
print(now.get_end_idx())
print(now.get_tagged_sentence())
'''
print(now.get_result())