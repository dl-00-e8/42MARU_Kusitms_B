#!python3
# -*- coding:utf-8 -*-

import re # 정규표현식 모듈
import redis # Redis 모듈

class regex:
    def __init__(self, input_data):
        # 사용할 변수목록 (list ver.)
        self.sentence = input_data
        self.entity_name = []
        self.value = []
        self.start_idx = []
        self.end_idx = []
        self.tagged_sentence = []
        
        '''
        # 사용할 변수목록 (not list ver.)
        self.sentence = input_data
        self.entity_name = '@null'
        self.value = 'null'
        self.start_idx = -1
        self.end_idx = -1
        self.tagged_sentence = 'notfound'
        '''

        # redis 서버 실행 후 DB 구축까지 과정 구현이 필요


    # 정규표현식 찾기
    def find_regex(self):
        # 정규표현식과 일치하는 문자열의 객체 주소 전달, finditer로 하면 result list에 object로 저장
        # finditer에 첫 번째 인자에 정규표현식이 들어가게 됨. Redis의 Key값을 끌고 오는 방향성으로 가자
        self.result = re.finditer('[0-9]+도', self.sentence)
        for i in self.result:            
            # start_idx와 end_idx, 일치문자열 정보 추출 완료
            # print(i.start(), i.end(), i.group())

            # list ver.
            # self.entity_name.append[엔트리네임]  Redis 구현되어야지 적용 가능
            self.value.append(i.group())
            self.start_idx.append(i.start())
            self.end_idx.append(i.end() - 1) # end_idx 리턴 값이 열린 구간으로 반환됨
            
            '''
            # not list ver.
            self.entity_name = '@sys.unit.temperature'
            self.value = i.group()
            self.start_idx = i.start()
            self.end_idx = i.end() - 1
            '''


    # 개체명 찾기 (re 모듈을 이용한 정규표현식 구현 부분)
    def get_entity_name(self):
        
        return self.entity_name


    # 해당되는 값 찾기
    def get_value(self):
        
        return self.value


    # 시작 인덱스 찾기
    def get_start_idx(self):
        
        return self.start_idx


    # 마지막 인덱스 찾기
    def get_end_idx(self):
        
        return self.end_idx


    # 해당 문장 변환
    def get_tagged_sentence(self):
        '''
        # not list ver.
        # start_idx와 end_idx, entity_name 변수 가지고와서 slicing 또는 새로운 변수 정의하는 방식으로 tagged_sentence 만들기
        self.tagged_sentence = self.sentence[0:self.start_idx] + self.entity_name + self.sentence[self.end_idx + 1:]
        '''

        # list ver.
        self.value.sort(key=len, reverse=True)
        for word in self.value:
            self.sentence = re.sub(word, self.entity_name, self.sentence)
            self.tagged_sentence = self.sentence

        return self.tagged_sentence


if __name__ == '__main__' :
    pass


