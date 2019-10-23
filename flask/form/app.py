from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/recieve')
def recieve():
    # request.args # output: {'username': 'nwith', 'message': 'hi'}
    username = request.args.get('username') # output: 'nwith'
    # message = request.args.get('message') # output: '안녕'
    menu = ['엽기떡볶이', '신전떡볶이', '응급실떡볶이', '죠스떡볶이']
    result = random.choice(menu)
    
    return render_template('recieve.html', user=username, result=result)

@app.route('/check_lotto')
def check_lotto():
    return render_template('check_lotto.html')

@app.route('/result_lotto')
def result_lotto():
    n = request.args.get('round_lotto')
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
    response = requests.get(url)
    lotto = response.json()
    winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]
    bonus = lotto['bnusNo']
    return render_template('result_lotto.html', winner=winner, bonus=bonus)

@app.route('/compare_lotto')
def compare_lotto():
    round_lotto = request.args.get('round_lotto')
    # numbers = list( map(int, request.args.get('numbers').split()) )
    numbers = [int(number) for number in request.args.get('numbers').split()]

    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={round_lotto}'
    response = requests.get(url)
    lotto = response.json()
    winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]
    bonus = lotto['bnusNo']
    
    matched = list( set(numbers) & set(winner) )
    count = len(matched)

    if count == 6:
        result = '1등 입니다'
    elif count == 5:
        if bonus in numbers:
            result = '2등 입니다'
        else:
            result = '3등 입니다'
    elif count == 4:
        result - '4등 입니다'
    elif count == 3:
        result = '5등 입니다'
    else:
        result = '꽝입니다...'

    return render_template('result_lotto.html', 
    winner=winner, bonus=bonus,round_lotto=round_lotto, numbers=numbers ,result=result)


if __name__ == '__main__':
    app.run(debug=True)