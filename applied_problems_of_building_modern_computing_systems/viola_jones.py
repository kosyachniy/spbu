import os

import cv2
from matplotlib import pyplot as plt


def viola_jones(image_path):
	face_cascade = cv2.CascadeClassifier(
		cv2.data.haarcascades + 'haarcascade_frontalface_default.xml',
	)
	eye_cascade = cv2.CascadeClassifier(
		cv2.data.haarcascades + 'haarcascade_eye.xml',
	)

	line_width = 3
	face_color = (0, 0, 255)
	eyes_color = (0, 255, 0)
	scale_factor = 1.1
	min_neighbors = 6

	img = cv2.imread(image_path)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(
		gray, scale_factor, min_neighbors,
	)

	for x, y, w, h in faces:
		img = cv2.rectangle(
			img, (x, y), (x + w, y + h), face_color, line_width,
		)

		roi_gray = gray[y : y + h, x : x + w]
		roi_color = img[y : y + h, x : x + w]

		eyes = eye_cascade.detectMultiScale(roi_gray)

		for ex, ey, ew, eh in eyes:
			cv2.rectangle(
				roi_color,
				(ex, ey),
				(ex + ew, ey + eh),
				eyes_color,
				line_width,
			)

	plt.imshow(img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	plt.show()


if __name__ == '__main__':
	ex_count = 8
	dataset = 1
	file = 'jpg'

	images = [
		os.path.join('data/ex{}'.format(dataset), '{}.{}'.format(i, file))
		for i in range(1, ex_count + 1)
	]

	for image in images:
		print('! {} !'.format(image))
		viola_jones(image)