# 우리가 자바스크립트에서 ajax를 써서 GET요청을 보냈던 것처럼
# 파이썬에서는 아래 코드처럼 requests 패키지를 이용하여 서울시 대기 OpenAPI에서 미세먼지 정보를 받아올 수 있습니다.

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# json형식으로 받아옴(request 패키지)
rjson = r.json()   

# {'RealtimeCityAir': {'list_total_count': 25, 'RESULT': {'CODE': 'INFO-000', 'MESSAGE': '정상 처리되었습니다'}, 'row': [{'MSRDT': '202201291400', 'MSRRGN_NM': '도심권', 'MSRSTE_NM': '중구', 'PM10': 29.0, 'PM25': 15.0, 'O3': 0.035, 'NO2': 0.01, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 55.0, 'ARPLT_MAIN': 'PM25'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '도심권', 'MSRSTE_NM': '종로구', 'PM10': 26.0, 'PM25': 16.0, 'O3': 0.036, 'NO2': 0.011, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '도심권', 'MSRSTE_NM': '용산구', 'PM10': 33.0, 'PM25': 18.0, 'O3': 0.037, 'NO2': 0.011, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'PM25'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '서북권', 'MSRSTE_NM': '은평구', 'PM10': 32.0, 'PM25': 17.0, 'O3': 0.036, 'NO2': 0.009, 'CO': 0.5, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '서북권', 'MSRSTE_NM': '서대문구', 'PM10': 32.0, 'PM25': 12.0, 'O3': 0.033, 'NO2': 0.01, 'CO': 0.3, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 53.0, 'ARPLT_MAIN': 'O3'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '서북권', 'MSRSTE_NM': '마포구', 'PM10': 24.0, 'PM25': 10.0, 'O3': 0.034, 'NO2': 0.014, 'CO': 0.4, 'SO2': 0.003, 'IDEX_NM': '보통', 'IDEX_MVL': 54.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '동북권', 'MSRSTE_NM': '광진구', 'PM10': 26.0, 'PM25': 14.0, 'O3': 0.036, 'NO2': 0.014, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '동북권', 'MSRSTE_NM': '성동구', 'PM10': 30.0, 'PM25': 13.0, 'O3': 0.035, 'NO2': 0.016, 'CO': 0.3, 'SO2': 0.003, 'IDEX_NM': '보통', 'IDEX_MVL': 55.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '동북권', 'MSRSTE_NM': '중랑구', 'PM10': 29.0, 'PM25': 18.0, 'O3': 0.017, 'NO2': 0.013, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 53.0, 'ARPLT_MAIN': 'PM25'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '동북권', 'MSRSTE_NM': '동대문구', 'PM10': 28.0, 'PM25': 12.0, 'O3': 0.037, 'NO2': 0.01, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '동북권', 'MSRSTE_NM': '성북구', 'PM10': 24.0, 'PM25': 11.0, 'O3': 0.034, 'NO2': 0.012, 'CO': 0.4, 'SO2': 0.003, 'IDEX_NM': '보통', 'IDEX_MVL': 54.0, 'ARPLT_MAIN': 'O3'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '동북권', 'MSRSTE_NM': '도봉구', 'PM10': 34.0, 'PM25': 13.0, 'O3': 0.036, 'NO2': 0.006, 'CO': 0.4, 'SO2': 0.003, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '동북권', 'MSRSTE_NM': '강북구', 'PM10': 31.0, 'PM25': 16.0, 'O3': 0.035, 'NO2': 0.008, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 55.0, 'ARPLT_MAIN': 'O3'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '동북권', 'MSRSTE_NM': '노원구', 'PM10': 22.0, 'PM25': 10.0, 'O3': 0.037, 'NO2': 0.01, 'CO': 0.4, 'SO2': 0.003, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '서남권', 'MSRSTE_NM': '강서구', 'PM10': 28.0, 'PM25': 11.0, 'O3': 0.036, 'NO2': 0.009, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '서남권', 'MSRSTE_NM': '구로구', 'PM10': 24.0, 'PM25': 8.0, 'O3': 0.035, 'NO2': 0.01, 'CO': 0.3, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 55.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '서남권', 'MSRSTE_NM': '영등포구', 'PM10': 25.0, 'PM25': 13.0, 'O3': 0.033, 'NO2': 0.009, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 53.0, 'ARPLT_MAIN': 'O3'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '서남권', 'MSRSTE_NM': '동작구', 'PM10': 31.0, 'PM25': 13.0, 'O3': 0.037, 'NO2': 0.01, 'CO': 0.4, 'SO2': 0.003, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '서남권', 'MSRSTE_NM': '관악구', 'PM10': 20.0, 'PM25': 9.0, 'O3': 0.031, 'NO2': 0.011, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 51.0, 'ARPLT_MAIN': 'O3'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '서남권', 'MSRSTE_NM': '금천구', 'PM10': 25.0, 'PM25': 18.0, 'O3': 0.039, 'NO2': 0.012, 'CO': 0.3, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 58.0, 'ARPLT_MAIN': 'PM25'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '서남권', 'MSRSTE_NM': '양천구', 'PM10': 25.0, 'PM25': 17.0, 'O3': 0.034, 'NO2': 0.01, 'CO': 0.4, 'SO2': 0.003, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'PM25'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '동남권', 'MSRSTE_NM': '강남구', 'PM10': 26.0, 'PM25': 14.0, 'O3': 0.034, 'NO2': 0.011, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 54.0, 'ARPLT_MAIN': 'O3'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '동남권', 'MSRSTE_NM': '서초구', 'PM10': 21.0, 'PM25': 12.0, 'O3': 0.037, 'NO2': 0.01, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 56.0, 'ARPLT_MAIN': 'O3'}, 
# {'MSRDT': '202201291400', 'MSRRGN_NM': '동남권', 'MSRSTE_NM': '송파구', 'PM10': 32.0, 'PM25': 15.0, 'O3': 0.03, 'NO2': 0.017, 'CO': 0.5, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 53.0, 'ARPLT_MAIN': 'PM25'}, {'MSRDT': '202201291400', 'MSRRGN_NM': '동남권', 'MSRSTE_NM': '강동구', 'PM10': 32.0, 'PM25': 17.0, 'O3': 0.027, 'NO2': 0.014, 'CO': 0.4, 'SO2': 0.004, 'IDEX_NM': '보통', 'IDEX_MVL': 54.0, 'ARPLT_MAIN': 'PM10'}]}}

print(rjson)
print(rjson['RealtimeCityAir']['row'][0]['NO2']) # 중구의 NO2 값

# 모든 구의 IDEX_MVL 값 프린트하기
gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    print(gu['MSRSTE_NM'], gu['IDEX_MVL'])

