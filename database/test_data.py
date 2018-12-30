from mongodb import *

import random, string
from hashlib import md5


def randomword(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

def insert(l):
	max_id = db['users'].find({}, {'id': True, '_id': False}).sort('id', -1)[0]['id'] + 1

	for i in range(l):
		obj = {
			'id': max_id + i,
			'login': randomword(5),
			'password': md5(randomword(10)),
			'name': randomword(7),
			'surname': randomword(5),
			'description': '',
			'rating': 0,
			'admin': 3,
			'ladders': {},
			'steps': [],
			'balance': 1000,
			'public': '',
		}

		db['users'].insert_one(obj)

if __name__ == '__main__':
	insert(int(input()))