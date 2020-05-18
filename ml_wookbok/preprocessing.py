from PIL import Image
import numpy as np

def data_to_label(data):
    age = int(data[8:10])
    label = answer_label(age)
    return label

def answer_label(age):
    if age < 18:
        label = 0 #18才未満
    elif age < 25:
        label = 1 #18才以上のaround20
    elif age <35:
        label = 2 # around30
    elif age < 45:
        label = 3 # around40
    elif age < 55:
        label = 4 # around50
    elif age < 65:
        label = 5 # around60
    else:
        label = 6 #65以上
    return label

def load_image(data):
    img = Image.open(data)
    img = img.convert('RGB')
    img = img.resize((224,224))
    img = np.asarray(img)
    img = img/255.0
    return img

def list_to_array(list1, list2):
    array1 = np.array(list1)
    array2 = np.array(list2)
    return array1, array2

def add_class_name(pred):
    pred_age = np.argmax(pred, axis = 1)
