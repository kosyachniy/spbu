import cv2
import numpy as np
import os
import random
from scipy import fftpack as sp
import typing as tp

IMAGE_COUNT = 11
PEOPLE_COUNT = 41


class Image:
    def __init__(self, image):
        self.image = image

    def descriptor(self, method, params):
        handler = getattr(self, method)
        return handler(params)

    @classmethod
    def image_read(cls, human, image_number):
        image = cv2.imread(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'orl_faces', 's' + str(human), str(image_number) + '.pgm',
            )
        )
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cls(image)

    def brightness_hist(self, params):
        image = self.image.reshape(
            (self.image.shape[0] * self.image.shape[1],),
        )
        hist = np.histogram(image, params)
        return hist[0]

    def dft(self, params):
        image = np.fft.fft2(self.image, norm='ortho')
        image = np.real(image)
        return self.reshape(image[:params, :params])

    def dct(self, params):
        image = sp.dct(self.image, axis=1)
        image = sp.dct(image, axis=0)
        return self.reshape(image[:params, :params])

    def scale(self, params):
        image = cv2.resize(
            self.image,
            (
                int(self.image.shape[1] * params),
                int(self.image.shape[0] * params),
            ),
        )
        return self.reshape(image)

    def gradient(self, params):
        shape = self.image.shape[0]
        i = 1
        result = []
        while i * params + 2 * params <= shape:
            prev_image = self.image[i * params : i * params + params, :]
            next_image = self.image[
                i * params + params : i * params + 2 * params, :,
            ]
            result.append(prev_image - next_image)
            i += 1
        result = np.array(result)
        result = result.reshape(
            (result.shape[0] * result.shape[1], result.shape[2]),
        )
        result = np.mean(result, axis=0)
        return result

    def __sub__(self, other):
        if isinstance(other, type(self)):
            raise TypeError
        return

    @staticmethod
    def reshape(image):
        return image.reshape((image.shape[0] * image.shape[1],))


class ImageStorage:
    storage = None

    @staticmethod
    def train_test_split(size):
        test_indexes = random.sample(range(1, IMAGE_COUNT), k=size)
        train_data = [
            i for i in ImageStorage.storage if i['image_number'] not in test_indexes
        ]

        return train_data, test_indexes

    @staticmethod
    def load_data(method, params):
        count = 0
        data = []
        for human in range(1, PEOPLE_COUNT):
            for image_number in range(1, IMAGE_COUNT):
                count += 1
                image = Image.image_read(human, image_number)
                result = image.descriptor(method, params)
                data.append(
                    {
                        'id': count,
                        'value': result,
                        'image': image.image,
                        'human': human,
                        'image_number': image_number,
                    },
                )
        ImageStorage.storage = data
        return data

    def _build_image_descriptors(self):
        pass
