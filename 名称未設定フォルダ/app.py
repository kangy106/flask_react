from flask import Flask, redirect, render_template, request, session, url_for
 
# Formクラス及び使用するフィールドをインポート
from wtforms import (
    Form, BooleanField, IntegerField, PasswordField, StringField,
    SubmitField, TextAreaField)
 
# 使用するvalidatorをインポート
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange

app = Flask(__name__)

# セッションで使用するシークレットキーを設定。本来はランダムな文字列が望ましい
app.config['SECRET_KEY'] = 'secret_key'

# wtformsのFormクラスを継承。それぞれの入力項目に対してバリデーションチェックをかける
class Ragistration(Form):
    name = StringField('名前：', validators=[DataRequired()])
    age = IntegerField('年齢：', validators=[NumberRange(0, 100, '不正な値です')])
    password = PasswordField('パスワード：', validators=[
                             Length(1, 10, '長さは1文字以上10文字以内です'),
                             EqualTo('re_password', 'パスワードが一致しません')])
    re_password = PasswordField('パスワード再入力：')
    comment = TextAreaField('コメント：')
    accept = BooleanField('内容確認：')
    submit = SubmitField('Submit')

# POSTかつバリデーションエラーがない場合は、セッションに入力内容を格納してregistered.htmlを表示
@app.route('/', methods=['GET', 'POST'])
def index():
    form = Ragistration(request.form)
    print(form.validate())
    if request.method == 'POST' and form.validate():
      session['name'] = form.name.data
      session['age'] = form.age.data
      session['comment'] = form.comment.data
      return redirect(url_for('registerd'))
    return render_template('register.html', form=form)

@app.route('/registered')
def registerd():
  return render_template('registered.html')
 
 
if __name__ == '__main__':
  app.run(debug=True)