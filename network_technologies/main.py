import sqlite3

db=sqlite3.connect('main.db')
with db:
	#Создаём
	db.execute("CREATE TABLE stocks (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, url text)")
	db.execute("CREATE TABLE currencies (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cont text, min real, max real, last real, stock int)")

	#Данные
	stocks = [
		['YoBit', 'http://yobit.net/'],
		['Bittrex', 'http://bittrex.com/'],
		['Poloniex', 'http://poloniex.com/']
	]
	currencies = [
		['BTC', 'BitCoin', 10, 7000, 6500, 1],
		['LTC', 'LiteCoin', 3000, 4000, 3300, 1],
		['ETH', 'Ethereum', 1000, 8000, 7200, 2],
		['DOGE', 'DogeCoin', 15, 27, 16, 1]
	]

	#Заполняем
	for i in stocks:
		db.execute("INSERT INTO stocks (name, url) VALUES (?, ?)", i)
	for i in currencies:
		db.execute("INSERT INTO currencies (name, cont, min, max, last, stock) VALUES (?, ?, ?, ?, ?, ?)", i)

	#Читаем
	for i in db.execute("SELECT * FROM stocks ORDER BY id DESC"):
		print(i)
	print('--------------------')
	for i in db.execute("SELECT * FROM currencies WHERE stock=1"):
		print(i)
	print('--------------------')
	for i in db.execute("SELECT * FROM currencies"):
		for j in db.execute("SELECT * FROM stocks WHERE id=?", (i[0],)):
			print(i[1] + ' - ' + j[1])