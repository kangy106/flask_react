from flask import Flask
from flask import render_template
#アプリケーションのインスタンスを生成
app = Flask(__name__)
#ルーティング urlを作る

bullets = [
    '箇条書き1',
    '箇条書き2',
    '箇条書き3',
    '箇条書き4',
    '箇条書き5',
    '箇条書き6'
    
]

@app.route("/america")
def america():
    return "<p>Hello, America!</p>"

@app.route("/world")
def world():
    return "<p>Hello, World!</p>"
#可変urls
@app.route("/japan/<city>")
def japan(city):
    #fStrings
    return render_template('hello.html', city=city, fruits=['orange','grape'], bullets=bullets)
#pythonの中にHTMLはよくない→templates
# html = '''
# <h1>サンプルHTML</h1>
# <ul>
#     <li>箇条書き1</li>
#     <li>箇条書き2</li>
#     <li>箇条書き3</li>
# </ul>
# '''

@app.route("/")
def hello():
    return render_template('hello.html')