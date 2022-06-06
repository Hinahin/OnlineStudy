from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {
			'username': 'Hin',
			'age': '33',
			}
	return render_template('index.html', title='Сервис для работы', user=user)
