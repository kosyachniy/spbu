import sqlite3
import re
import datetime

NAME_DB = 'students'

db = sqlite3.connect(NAME_DB + '.db')

def create(dbname=NAME_DB):
	with db:
		db.execute("CREATE TABLE " + dbname + " (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, surname text, acgroup INTEGER, description text, year INTEGER)")

def insert_user(name, surname, acgroup, year, description='', dbname=NAME_DB):
	if not re.match(r'^[a-zA-Zа-яА-Я ]*$', name):
		print('Invalid name!')

	elif not re.match(r'^[a-zA-Zа-яА-Я ]*$', surname):
		print('Invalid surname!')

	elif type(acgroup) != int:
		print('Invalid group!')

	elif type(year) != int or year < 1990 or year > datetime.datetime.now().year:
		print('Invalid year!')

	else:
		with db:
			db.execute("INSERT INTO " + dbname + " (name, surname, acgroup, description, year) VALUES ((?), (?), (?), (?), (?))", (name, surname, acgroup, description, year))

def read(dbname=NAME_DB, **pol):
	with db:
		req = "SELECT * FROM " + dbname

		f = True
		for i in pol:
			if type(pol[i]) == int:
				pol[i] = str(pol[i])
			elif type(pol[i]) == str:
				pol[i] = "'" + pol[i] + "'"
			
			if f:
				req += " WHERE "
				f = False
			else:
				req += " AND "

			req += i + "=" + pol[i]

		for i in db.execute(req):
			print('%s %s\nGroup: %d (%d year)\n%s' % (i[2], i[1], i[3], i[5], i[4]), '-'*100, sep='\n')