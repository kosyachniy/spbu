import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.fftpack import dct
from PIL import Image
from numpy import random


def get_histogram(image: np.ndarray, param=30):
    hist, _ = np.histogram(image, bins=np.linspace(0, 1, param))
    return hist


def get_dft(image, mat_side=13):
    f = np.fft.fft2(image)
    f = f[0:mat_side, 0:mat_side]
    return np.abs(f)


def get_dct(image, mat_side=13):
    c = dct(image, axis=1)
    c = dct(c, axis=0)
    c = c[0:mat_side, 0:mat_side]
    return c


def get_random_points(image, points):
    res = np.array([image[point[0][0], point[0][1]] for point in points])
    return res


def get_gradient(image, n=2):
    shape = image.shape[0]
    i, l = 0, 0
    r = n
    result = []

    while r <= shape:
        window = image[l:r, :]
        result.append(np.sum(window))
        i += 1
        l = i * n
        r = (i + 1) * n
    result = np.array(result)
    return result


def get_scale(image, scale=0.35):
    h = image.shape[0]
    w = image.shape[1]
    new_size = (int(h * scale), int(w * scale))
    image = np.array(Image.fromarray(image).resize(new_size))
    return image



if __name__ == "__main__":
    name = 'photos/valid_40_5.pgm'
    img = cv2.imread(name, 0)
    # example_hist, _ = get_histogram(img)

    example_dft = get_dft(img)[0]


    names = ['1_1', '2_2', '5_3', '21_8', '26_4', '31_8', '32_5', '32_10', '40_2', '40_10']
    dists = []
    for name in names:
        name = 'photos/photos_for_valid/' + name + '.pgm'
        img = cv2.imread(name, 0)
        cv2.imshow('name', img)
        dft = get_dft(img)[0]
        dist = np.linalg.norm(example_dft - dft, ord=2)
        dists.append(dist)
    print(names[np.argmin(dists)], ':', min(dists))
