# 42MARU_Kusitms_B
42MARU 기업프로젝트 개발과제

<br>

## 팀원
|이정진|박형준|이아린|정재희|
|:---:|:---:|:---:|:---:|
|[dl-00-e8](https://github.com/dl-00-e8)||[Arin0421](https://github.com/Arin0421)|[JAEHEE25](https://github.com/JAEHEE25)|  

<br>

## 목차
1. 언어 및 라이브러리, 데이터베이스
2. Redis 사용 엔티티
3. Output 반환 형식
4. 디렉토리 구성
5. pytest 사용 방법

<br>

## 내용

###  1. 언어 및 라이브러리, 데이터베이스
언어 : Python  
라이브러리 : re, pytest_bdd, redis  
데이터베이스 : Redis

### 2. Redis 사용 엔티티
- @sys.city : '해외도시명'
- @sys.state : '해외 주 단위'
- @sys.location : '국내 지역'
- @sys.nation : '국가명'
- @sys.currency.name : '통화명'
- @sys.currency.code : '통화 코드'
- @sys.unit.currency : '통화'

Redis 사용 엔티티 선정 방식 : 사전적으로 정리가 필요하고, 추가적으로 변경 가능성이 높은 경우

### 3. Output 반환 형식
모듈 기준
- 항목별 모든 Output을 하나의 리스트를 통해 반환  
- 항목별 Output을 각각 메소드를 사용하여 반환 (구현 목적 : pytest 활용)


### 4. 디렉토리 구성


### 5. pytest 사용 방법과 예시
(1) tc.feautre 파일에 input과 예상 output을 변경

(2) 해당 디렉토리에서 py.test 진행


#### Input 기본 형식

#### Input 변경 에시

#### Output (Success case)

#### Output (Fail case)
