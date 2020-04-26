import os

import cv2
from matplotlib import pyplot as plt


def template_matching(temp, ex):
	methods = ['cv2.TM_CCOEFF_NORMED']
	image = cv2.imread(ex, 0)
	template = cv2.imread(temp, 0)
	w, h = template.shape[::-1]

	for meth in methods:
		img = image.copy()
		method = eval(meth)

		res = cv2.matchTemplate(img, template, method)
		min_val, max_val, min_loc, top_left = cv2.minMaxLoc(res)
		bottom_right = (top_left[0] + w, top_left[1] + h)

		cv2.rectangle(img, top_left, bottom_right, 0, 5)

		plt.subplot(121)
		plt.imshow(res, cmap='gray')
		plt.title('Matching Result')
		plt.xticks([]), plt.yticks([])
		plt.subplot(122)
		plt.imshow(img, cmap='gray')
		plt.title('Detected Point')
		plt.xticks([])
		plt.yticks([])
		plt.suptitle(meth)
		plt.show()


def process_entity(ex_count, temp_count, ex_folder, temp_folder, file):
    images = [
        os.path.join(ex_folder, '{}.{}'.format(i, file))
        for i in range(1, ex_count + 1)
    ]

    templates = [
        os.path.join(temp_folder, f'{i}.png')
        for i in range(1, temp_count + 1)
    ]

    for template in templates:
        for image in images:
            print(f'finding {template} in {image}')
            template_matching(template, image)


if __name__ == '__main__':
	temp_count = 3
	ex_count = 8
	dataset = 1

	process_entity(
		ex_count=ex_count,
		temp_count=temp_count,
		ex_folder='data/ex{}'.format(dataset),
		temp_folder='data/temp{}'.format(dataset),
		file='jpg',
	)
