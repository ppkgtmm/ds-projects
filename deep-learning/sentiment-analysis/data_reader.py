import numpy as np
import bz2

def get_labels_and_texts(file, data_size):
    labels = []
    texts = []
    i = 0
    for line in bz2.BZ2File(file):
        if i == data_size:
            break
        i += 1
        x = line.decode("utf-8")
        labels.append(int(x[9]) - 1)
        texts.append(x[10:].strip())
    return np.array(labels), np.array(texts)