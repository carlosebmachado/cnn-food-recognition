# -*- coding: utf-8 -*-
import sys
from keras_preprocessing import image
from keras.models import model_from_json
import PySimpleGUI as sg
import numpy as np
import json
import cv2
import matplotlib.pyplot as plt


# desabilita a notação ciêntifica
np.set_printoptions(precision=5, suppress=True)
with open('model/meta.json', 'r') as json_file:
    meta = json.load(json_file)

IMG_SIZE = meta['model_config']['img_size']
NUM_CHANNELS = meta['model_config']['num_channels']

class_indices = meta['class_indices']
for i in range(len(class_indices)):
    class_indices[i] = class_indices[i].replace('_', ' ')
    class_indices[i] = class_indices[i].capitalize()

# carrega o modelo
json_file = open('model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('model/model.h5')


# prepara a img
img = image.load_img('dataset/test_images/caesar_salad/01.png',
                          target_size=(IMG_SIZE,IMG_SIZE))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
test_img = image.img_to_array(img)
if NUM_CHANNELS == 1:
    test_img=cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
test_img /= 255
if NUM_CHANNELS == 1:
    test_img = np.expand_dims(test_img, axis=2)
test_img = np.expand_dims(test_img, axis=0)

# prediz a classe
result = model.predict(test_img)

# encontra o index da classe
i = 0
index = 0
big = result[0][0]
for i in range(len(result[0])):
    if result[0][i] > big:
        index = i
        big = result[0][i]

print('Resultado: {}.'.format(result))
print('Classe: {}.'.format(class_indices[index]))
plt.imshow(img)
