from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/mulcam')
def mulcam():
    return 'This is mulcam!!!'

# Path Variable / Variable Routing
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'Hi, {name}' # 3.6 이전 버전: 'Hi, {}'.format(name)

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'{num}의 세제곱은 {result}입니다.' # 문자로만 리턴할 수 있다.

import random
# 사람 수를 Path를 통해 입력 받아, 사람 수 만큼 메뉴 추천
@app.route('/dinner/<int:person>')
def dinner(person):
    menu = ['후라이드치킨', '양념치킨', '간장치킨', '고추바사삭', '뿌링클', '황금올리브']
    result = random.sample(menu, person)
    return ','.join(result)

@app.route('/html')
def html():
    return """
    <h1> Hi, Hello</h1>
    """

@app.route('/html_file')
def html_file():        
    return render_template('file.html')

# Template Variable
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name=name)


@app.route('/list')
def list1():
    menu = ['후라이드치킨', '양념치킨', '간장치킨', '고추바사삭', '뿌링클', '황금올리브']
    return render_template('list.html', menu=menu)




if __name__ == '__main__':
    app.run(debug=True)