# IDEX_MVL 값이 60 미만인 구의 이름과 값 프린트하기

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    if gu['IDEX_MVL'] < 60:
        print (gu['MSRSTE_NM'], gu['IDEX_MVL'])