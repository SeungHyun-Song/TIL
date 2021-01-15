# 공공 데이터 API 활용 실습 (대기오염정보)

# 1. 필요한 라이브러리 import 하기
import requests, pprint

# 2. API URL 및 KEY값 확인
serviceKey = 'J2OME6IM%2FIg2OlWh7nHRcZbJ8rqlABFwt%2BUMtb%2BtQff78PgWqOKtgHI5qpsmJkL7JAowEdyy0Agx6kFUa690rA%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={serviceKey}&sidoName=광주&returnType=json'


# 3. 요청 및 응답값 확인
response = requests.get(url).json()
# pprint.pprint(response)


sido_name = response['response']['body']['items'][2]['sidoName']
pm_10 = response['response']['body']['items'][2]['pm10Value']
station_name = response['response']['body']['items'][2]['stationName']


# 4. 최종 출력 문자열
# '__의 미세먼지 농도는 __입니다. (측정소 : ___)'

text = f'{sido_name}의 미세먼지 농도는 {pm_10}입니다. (측정소 : {station_name})'

# 5. 텔레그램 메시지 전송 (sendMessage)

token = '1594549820:AAHu6zljOvz9RFfLvPM51tdGUk_wCpmJMdM'
chat_id = '1583083126'

telegram_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(telegram_url)






