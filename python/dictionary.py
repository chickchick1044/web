lunch = {
    '중국집': '양자강', # trailing comma
    '한식집': '시래기'
}
# lunch = dict(중국집='양자강')

lunch['분식집'] = '김밥까페'
lunch['중국집'] # 'output': '양자강'

dinner = {
    '한식집': { # key: string, integer, float, boolean
        '고갯마루': '02-3476-7006',
        '순남시래기': '02-1234-1234',

    }
}

dinner['한식집']['고갯마루'] # output: 02-3476-7006
dinner.get('한식집').get('고갯마루')
# 두 방식의 차이
# []로 접근할 경우, 존재하지 않는 키를 사용하면 오류
# .get으로 접근할 경우, 존재하지 않는 키를 사용하면 None을 리턴

# 딕셔너리 기본 활용 (반복문)
for key in lunch:
    # print(key)
    print(lunch.get(key))

# key 값 가져오기
for key in lunch.keys(): # [key, key, ...]
    print(key)

# value 값 가져오기
for value in lunch.values(): # [value, value, ...]
    print(value)

# key, value 값 가져오기         # 리스트 안에 튜플 형태로 존재
for key,value in lunch.items(): # [(key, value), (key, value), ...] 
    print(key, value)

