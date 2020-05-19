import numpy as np
from tqdm import tqdm
from PIL import Image
from keras.utils.np_utils import to_categorical
class TrainProcess:
    def __init__(self,train_data):
        self.train_data = train_data

    def process(self):
        X_train, y_train = [], []
        for data in tqdm(self.train_data[:7900]):
            train_img = load_image(data)
            X_train.append(train_img)
            train_y = data_to_label(data)
            y_train.append(train_y)
        X_train =list_to_array(X_train)
        y_train =list_to_array(y_train)
        y_class = to_categorical(y_train)
        return X_train, y_class


class TestProcess:
    pass

def data_to_label(data):
    age = int(data[7:9])
    label = age_to_label(age)
    return label


def load_image(data):
    img = Image.open(data)
    img = img.convert('RGB')
    img = img.resize((224, 224))
    img = np.asarray(img)
    img = img / 255.0
    return img



def list_to_array(list):
    array = np.array(list)
    return array

def age_to_label(age):
    if age < 18:
        label = 0
    elif age < 22:
        label = 1
    elif age < 26:
        label = 2
    elif age < 30:
        label = 3
    elif age < 35:
        label = 4
    elif age < 40:
        label = 5
    elif age < 45:
        label = 6
    elif age < 50:
        label = 7
    elif age < 55:
        label = 8
    elif age < 60:
        label = 9
    elif age < 65:
        label = 10
    else:
        label = 11
    return label
