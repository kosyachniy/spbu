import math
import numpy as np
from matplotlib import pyplot as plt

from image import Image, ImageStorage
from settings import *


def distance(x, y):
    return np.sum((x - y) ** 2)


TEST_SIZE = list(range(1, 10))


def show_images(
        method,
        my_image,
        found_image,
        descriptive_my_image,
        descriptive_found_image,
        params,
):
    plt.subplot(221)
    plt.imshow(my_image, cmap='gray')
    plt.title('My image')

    plt.subplot(222)
    plt.imshow(found_image, cmap='gray')
    plt.title('Detected Point')

    if method not in ['brightness_hist', 'gradient']:
        if method == 'scale':
            params = reshapes[str(params)]
        else:
            params = (params, params)
        descriptive_my_image = descriptive_my_image.reshape(params)
        descriptive_found_image = descriptive_found_image.reshape(params)

        plt.subplot(223)
        plt.imshow(descriptive_my_image, cmap='gray')
        plt.title('My image descriptor')

        plt.subplot(224)
        plt.imshow(descriptive_found_image, cmap='gray')
        plt.title('Detected Point descriptor')
    else:
        plt.subplot(223)
        plt.hist(descriptive_my_image)
        plt.title('My image descriptor')

        plt.subplot(224)
        plt.hist(descriptive_found_image)
        plt.title('Detected Point descriptor')

    plt.show()


class Classifier:
	def __init__(self):
		pass

	def worker(self, image, train_data, with_image, method, params):
		detection_results = []
		for i, face in enumerate(train_data):
			dist = distance(face['value'], image['value'])

			detection_results.append(dist)

		detected_point_ind = np.array(detection_results).argmin()
		found_image = train_data[detected_point_ind]['image']
		descriptive_found_image = train_data[detected_point_ind]['value']
		my_image = image['image']
		descriptive_my_image = image['value']

		if with_image:
			show_images(
				method,
				my_image,
				found_image,
				descriptive_my_image,
				descriptive_found_image,
				params,
			)
		return train_data[detected_point_ind]['human']

	def find_nearest_face(self, method, params, test_size, with_images=False):
		prepared_data = ImageStorage.load_data(method, params)
		train_data, test_indexes = ImageStorage.train_test_split(
			test_size,
		)
		count = 0
		predicted = []
		for i, image in enumerate(prepared_data):
			if image['image_number'] in test_indexes:
				answer = self.worker(
					image, train_data, with_images, method, params,
				)

				predicted.append(int(answer == image['human']))
				count += 1
		accuracy = sum(predicted) / count
		print(round(accuracy, 3), 'param: ', params, 'test_size: ', test_size)
		return accuracy, predicted

	def vote(self):

		# plt.title("Closest images")

		votes_prediction = []
		for method in ['brightness_hist', 'dft', 'dct', 'gradient']:
			current_votes_prediction = []
			results = []
			for test_size in TEST_SIZE:
				accuracy = 0
				for _ in range(5):
					res, predicted = self.find_nearest_face(method, best_params[method], test_size)
					accuracy += res

				results.append(accuracy / 5)
				current_votes_prediction.append(predicted)

				# print(current_votes_prediction)
				# # HHH.append(l_all)
				# ax1 = plt.subplot(414)
				# ax1.plot(list(range(1, len(current_votes_prediction)+1)), current_votes_prediction)
				# plt.draw()
				# plt.pause(0.01)
				# plt.clf()

			votes_prediction.append(current_votes_prediction)
			meth = {
				'brightness_hist': 'Гистограмма яркости',
				'dft': 'DFT',
				'dct': 'DCT',
				'gradient': 'Градиент',
				'scale': 'Scale',
			}
			# par = {
			# 	'brightness_hist': [0.5413105413105413, 0.6858974358974359, 0.7545787545787546, 0.8076923076923077, 0.882051282051282, 0.9294871794871795, 0.9743589743589743, 0.9743589743589743],
			# 	'dft': [0.46153846153846156, 0.6314102564102564, 0.717948717948718, 0.7905982905982906, 0.8615384615384616, 0.9102564102564102, 0.9230769230769231, 0.9615384615384616],
			# 	'dct': [0.6353276353276354, 0.7692307692307693, 0.7912087912087912, 0.8974358974358975, 0.9538461538461539, 0.9615384615384616, 0.9743589743589743, 0.9871794871794872],
			# 	'gradient': [0.5384615384615384, 0.6153846153846154, 0.684981684981685, 0.7435897435897436, 0.8256410256410256, 0.8333333333333334, 0.8205128205128205, 0.8589743589743589],
			# 	'scale': [0.6866096866096866, 0.8269230769230769, 0.8827838827838828, 0.9444444444444444, 0.9487179487179487, 0.9615384615384616, 0.9743589743589743, 0.9615384615384616],
			# }
			plt.plot(TEST_SIZE, list(reversed(results)), label=meth[method])
			# plt.plot([i * 40 for i in TEST_SIZE], list(reversed(results)), label=meth[method])
			# plt.plot([i * 40 for i in TEST_SIZE[:-1]], par[method], label=meth[method])

		accuracies = []
		voting_accuracies = np.array(votes_prediction)
		for col in range(voting_accuracies.shape[1]):
			ls_len = len(voting_accuracies[:, col][0])
			res = np.zeros(ls_len)
			for ls in voting_accuracies[:, col]:
				res += np.array(ls)
			count = 0
			for i in res:
				if i >= 2:
					count += 1
			accuracies.append(count / res.shape[0])

			# print(accuracies)
			# # HHH.append(l_all)
			# ax1 = plt.subplot(414)
			# ax1.plot(list(range(1, len(accuracies)+1)), accuracies)
			# plt.draw()
			# plt.pause(0.01)
			# plt.clf()

		# plt.plot([i * 40 for i in TEST_SIZE[:-1]], list(reversed(accuracies))[1:])
		plt.plot(TEST_SIZE, list(reversed(accuracies)), label='Голосование')
		# plt.plot([i * 40 for i in TEST_SIZE], list(reversed(accuracies)), label='Голосование')
		# plt.ylim((0.6,1.1))
		# plt.plot([i * 40 for i in TEST_SIZE[:-1]], list(reversed(accuracies))[1:], label='Голосование')
		# plt.plot([i * 40 for i in TEST_SIZE[:-1]], [0.7166666666666667, 0.840625, 0.9, 0.9708333333333333, 0.98, 0.99375, 1.0, 0.9875], label='Голосование')

		plt.legend(title='Методы:')
		plt.xlabel("Размер")
		plt.ylabel("Точность")
		plt.show()
		# plt.close(fig)

	def cross_val(self, method, params, cross_validation_iteration=3, with_images=False):
		accuracies = []
		for test_size in TEST_SIZE:
			for param in params:
				cross = 0
				for _ in range(cross_validation_iteration):
					val, _ = self.find_nearest_face(method, param, test_size)
					cross += val
				accuracies.append((cross / cross_validation_iteration, param, test_size))

		accuracies = np.array(accuracies)
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.scatter(np.array(accuracies[:, 1]), np.array(accuracies[:, 2]), np.array(accuracies[:, 0]), c='r',
					marker='o')
		# ax.set_xlabel('Params')
		ax.set_ylabel('Размер')
		ax.set_zlabel('Точность')
		plt.show()

		print('CROSS VAL BEST ESTIMATOR', max(accuracies, key=lambda i: i[0]))

if __name__ == '__main__':
	classifier = Classifier()
	classifier.vote()