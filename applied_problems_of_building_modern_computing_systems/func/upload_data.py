from skimage import io

def facedataset(set):
    train = []
    datasets = []
    labels = [i for i in range(set)]
    for i in range(1, set+1):
        img = io.imread("data/orl_faces/s%i/%i.pgm" % (i, 1))
        train.append(img)
        dataset=[]
        
        for j in range(2, 11):
            img = io.imread("data/orl_faces/s%i/%i.pgm" % (i, j))
            dataset.append(img)
        datasets.append(dataset)
    return datasets, labels, train 