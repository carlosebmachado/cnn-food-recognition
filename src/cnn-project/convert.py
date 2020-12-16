# -*- coding: utf-8 -*-
from keras.models import model_from_json
import tensorflow as tf


# carrega o modelo
json_file = open('model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('model/model.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open('model/model.tflite', 'wb').write(tflite_model)
