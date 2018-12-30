import unittest

from index import MongoClient, connect, get_reviews, add_history, add_reviews


class TestCase(unittest.TestCase):
	def test_db_connect(self):
		res = connect()

		self.assertEqual(type(res), MongoClient)

		self.assertEqual(res._MongoClient__all_credentials['admin'].source, 'admin')
		self.assertEqual(res._MongoClient__all_credentials['admin'].username, 'root')
		self.assertEqual(res.server_info()['ok'], 1.0)

	def test_get_reviews(self):
		res = get_reviews()

		self.assertEqual(type(res), list)
		self.assertEqual(len(res), 3)

		for i in res:
			self.assertEqual(type(i), dict)
			self.assertEqual(set(i), {'id', 'name', 'cont'})

			self.assertEqual(type(i['id']), int)
			self.assertEqual(type(i['name']), str)
			self.assertEqual(type(i['cont']), str)

	def test_insert_data(self):
		data = {
			'name': 'Имя',
			'mail': 'polozhev@mail.ru',
			'count': 0.024,
			'card': 1234123412341234,
			'course': 226378,
			'referal': 'referal',
		}
		self.assertEqual(add_history(data), None)

		with self.assertRaises(Exception):
			data = {
				'name': 'Имя',
				'mail': 'polozhev@.ru',
				'count': 0.48,
				'card': 1234123412341234,
				'course': 226378,
				'referal': 'referal',
			}
			add_history(data)

			data = {
				'name': 'Имя',
				'mail': 'polozhev@a.ru',
				'count': 0.552,
			}
			add_history(data)

			data = {
				'name': 12,
				'mail': 'polozhev@.ru',
				'count': 0.024,
				'card': 1234123412341234,
			}
			add_history(data)

	def test_add_review(self):
		with self.assertRaises(Exception):
			data = {
				'name': 123,
				'cont': 'Комментарий',
			}
			add_reviews(data)

			data = {
				'name': 'Alex',
				'comt': 'Комментарий',
			}
			add_reviews(data)



if __name__ == '__main__':
	unittest.main()