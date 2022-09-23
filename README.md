# 42MARU_Kusitms_B
시스템에 등록된 개체명을 특정 문장에서 추출하는 python module 개발

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
42MARU_Kusitms_B:.  
|   README.md  
|   tc.feature  
|   test_fixture.py   
|               
+---Module  
　　|   regex.py
        

### 5. pytest 사용 방법과 예시
확인 필수 환경 : Redis 서버 실행 여부 (실행 중이여야 작동)  
Redis 설치 필요 시, [설치 페이지](https://github.com/microsoftarchive/redis/releases)로 접속하여, msi 파일 다운로드 진행

#### 사용 방법
(1) tc.feautre 파일에 input과 예상 output을 변경

(2) 해당 디렉토리에서 py.test 진행

(3) - 1. testcase 성공 시, 아래 Output (Success case)와 같이 출력

(3) - 2. testcase 성공 시, 아래 Output (Fail case)와 같이 출력 / E와 함께 작성된 붉은색 문장이 에러 위치 및 내용 제공

#### 예시
**Input Form**  
![input_form](https://user-images.githubusercontent.com/76556999/191917756-ee1b0a8c-6d26-4e8c-b477-16329c475dd7.png)

**Input Example**  
![input_exmaple](https://user-images.githubusercontent.com/76556999/191917751-51360588-7374-40c1-958a-098f0c19e2d1.png)

**Output (Success case)**  
![success_case](https://user-images.githubusercontent.com/76556999/191917758-f1b11072-eb76-47fd-b4a7-1728e681e3bf.png)

**Output (Fail case)**  
![fail_case](https://user-images.githubusercontent.com/76556999/191917744-71292622-afc3-4f12-8217-ec53fff9da8c.png)
