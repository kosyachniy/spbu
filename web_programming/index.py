from flask import Flask, render_template, request
from pymongo import MongoClient

import time
import json
import re


app = Flask(__name__)

def connect():
	return MongoClient('mongodb://root:asdrqwerty09@invo-shard-00-00-guyjh.mongodb.net:27017,invo-shard-00-01-guyjh.mongodb.net:27017,invo-shard-00-02-guyjh.mongodb.net:27017/INVO?ssl=true&replicaSet=INVO-shard-0&authSource=admin')
db = connect()['exchanger']

def add_history(req):
	if len({'name', 'mail', 'count', 'card'} & set(req)) != 4:
		raise Exception('Не все поля заполнены!')

	if type(req['name']) != str:
		raise Exception('Неправильно заполненно поле "name"')

	temp = re.compile(r'\S+@\S+\.\S+')
	if type(req['mail']) != str or temp.match(req['mail']) == None:
		raise Exception('Неправильно заполнено поле "mail"')

	if type(req['count']) not in (int, float):
		raise Exception('Неправильно заполнено поле "count"')

	if len(str(req['card'])) != 16:
		raise Exception('Неправильно заполнено поле "card"')

	req['time'] = time.time()

	db['history'].insert_one(req)

def add_reviews(req):
	if len({'name', 'cont'} & set(req)) != 2:
		raise Exception('Не все поля заполнены!')

	if type(req['name']) != str:
		raise Exception('Неправильно заполненно поле "name"')

	if type(req['cont']) != str:
		raise Exception('Неправильно заполненно поле "cont"')

	req['time'] = time.time()

	try:
		req['id'] = db['reviews'].find().sort('id', -1)[0]['id'] + 1
	except:
		req['id'] = 1

	db['reviews'].insert_one(req)

# Получить отзывы

def get_reviews():
	return [i for i in db['reviews'].find({}, {'_id': False, 'time': False})][-3:][::-1]


@app.route('/')
def index():
	referal = request.args.get('action')
	if not referal:
		referal = ''

	return render_template('index.html',
		url = '',

		news = True,
		reviews = get_reviews(),
		message = 'Перевод из RUB в BTC из-за большой нагрузки временно недоступен!',
		referal = referal,
	)

@app.route('/rules')
@app.route('/rules/')
def rules():
	return render_template('rules.html',
		url = 'rules',

		news = False,
		reviews = get_reviews(),
		message = None,
	)

@app.route('/confirm')
@app.route('/confirm/')
def confirm():
	return render_template('confirm.html',
		url = 'confirm',

		news = False,
		reviews = get_reviews(),
		message = None,
	)

@app.route('/sys_change')
@app.route('/sys_change/')
def sys_change():
	course = request.args.get('cur')
	course = float(course) if course else 0.0

	referal = request.args.get('ref')
	if not referal:
		referal = ''

	req = {
		'name': request.args.get('name'),
		'mail': request.args.get('mail'),
		'count': float(request.args.get('count').replace(',', '.')),
		'card': request.args.get('card'),
		'course': course,
		'referal': referal,
	}

	add_history(req)

	return '<script>document.location.href = "/confirm/"</script>'

@app.route('/sys_reviews')
@app.route('/sys_reviews/')
def sys_reviews():
	req = {
		'name': request.args.get('name'),
		'cont': request.args.get('cont'),
	}

	add_reviews(req)

	return '<script>document.location.href = "/"</script>'

@app.route('/testing')
@app.route('/testing/')
def testing():
	return render_template('testing.html')


if __name__ == '__main__':
	app.run(debug=True)