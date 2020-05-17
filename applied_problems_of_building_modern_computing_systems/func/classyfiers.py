import sklearn.datasets
import numpy as np
import scipy.fftpack as dct
import random
import cv2

from skimage.transform import rescale

scalar = sklearn.preprocessing.MaxAbsScaler()

def H_clsf(img1, img2):

    size=10;
    
    img1_h = cv2.calcHist([img1],[0],None,[size],[0,256])
    img2_h = cv2.calcHist([img2],[0],None,[size],[0,256])

    return np.linalg.norm(img2_h - img1_h) #расстояние как норма вектора разности

def DFT_clsf(img1, img2):
    
    img1 = scalar.fit_transform(np.array(img1, 'float64'))
    img2 = scalar.fit_transform(np.array(img2, 'float64'))
    img1_dft = np.fft.rfftn(img1)
    img2_dft = np.fft.rfftn(img2)

    return np.linalg.norm(img2_dft - img1_dft)

def DCT_clsf(img1, img2):
    img1 = scalar.fit_transform(np.array(img1, 'float64'))
    img2 = scalar.fit_transform(np.array(img2, 'float64'))
    img1_dct = dct.dct(dct.dct(img1))
    img2_dct = dct.dct(dct.dct(img2))

    return np.linalg.norm(img2_dct - img1_dct )


def G_clsf(img1, img2):
    
    _ksize=7;
    
    img1_g = cv2.Sobel(img1,cv2.CV_64F,0,1,ksize=_ksize).mean(axis=0)
    img2_g = cv2.Sobel(img2,cv2.CV_64F,0,1,ksize=_ksize).mean(axis=0)

    return np.linalg.norm(np.array(img2_g) - np.array(img1_g))

def Scale_clsf(img1, img2):
    s=2
    img1_scl = rescale(img1, 1/s, mode='constant', anti_aliasing=False, multichannel=False)
    img2_scl = rescale(img2, 1/s, mode='constant', anti_aliasing=False, multichannel=False)


    return np.linalg.norm(np.array(img2_scl) - np.array(img1_scl))


def RP_clsf(img1, img2):
    random.seed(0)
    p=950
    h,w = img1.shape
    points = []
    for i in range(p):
        points.append([random.randint(0, h - 1), random.randint(0, w - 1)])

    img1_rp = [img1[i,j] for i,j  in points]
    img2_rp = [img2[i,j] for i,j in points]
    
    return np.linalg.norm(np.array(img2_rp) - np.array(img1_rp))



