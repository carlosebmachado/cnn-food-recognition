from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from keras.models import model_from_json
import json
import os
import cv2
import numpy as np
import time as t
import datetime
import matplotlib.pyplot as plt



# CONSTANTES E VARIÁVEIS -----------------------------------------------------

DEBUG = False
LOAD = False
COLOR = 3
GRAY = 1

IMG_SIZE = 128
NUM_CHANNELS = COLOR
BATCH_SIZE = 128
EPOCHS = 30


# CARREGA E PREPADA OS DADOS -------------------------------------------------
# pega o diretório de trabalho atual
PATH = os.getcwd()
# define o caminho do dataset
data_path = PATH + '/dataset/images'
if DEBUG:
    data_path += '_100'
# pega a lista de classes
data_dir_list = os.listdir(data_path)

# quantidade de imagens em cada classe
img_amt_class = []

# loop para garregamento das imagens
img_data_list = []
for dataset in data_dir_list:
    img_list = os.listdir(data_path+'/'+ dataset)
    print ('Loading images of {} class.'.format(dataset))
    # adiciona um novo contador
    img_amt_class.append(0)
    for img in img_list:
        # contabiliza a img
        img_amt_class[-1] += 1
        # carrega, redimensiona e add
        input_img = cv2.imread(data_path + '/'+ dataset + '/'+ img )
        input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
        #plt.imshow(input_img)
        if NUM_CHANNELS == GRAY:
            input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
        input_img_resize = cv2.resize(input_img,(IMG_SIZE,IMG_SIZE))
        img_data_list.append(input_img_resize)
# converte para dado utilizável e escala o byte para 1
img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data /= 255

if NUM_CHANNELS == GRAY:
    img_data = np.expand_dims(img_data, axis=3)

print ('Data shape: {}.'.format(img_data.shape))
print('Found classes: {}.'.format(data_dir_list))
print('Num of images by class: {}.'.format(img_amt_class))

# define as labels
labels = np.ones(sum(img_amt_class), dtype='int64')
c, i = 0, 0
for amt in img_amt_class:
    labels[c: amt + c] = i
    i += 1
    c += amt
# converte para categórico
cat = np_utils.to_categorical(labels, len(img_amt_class))
# embaralha
x, y = shuffle(img_data, cat)
# separa o dataset
x_train, x_test, y_train, y_test = train_test_split(x, y)


# CRIA E TREINA A CNN --------------------------------------------------------
model = Sequential()

if LOAD:
    json_file = open('model/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights('model/model.h5')
else:
    # adiciona as camadas convulocionais
    model.add(Conv2D(32, (3, 3),
                     input_shape = (IMG_SIZE, IMG_SIZE, NUM_CHANNELS),
                     activation = 'relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(64, (3, 3),
                     activation = 'relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(128, (3, 3),
                     activation = 'relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    # flatten
    model.add(Flatten())
    
    # adiciona as camadas densas
    model.add(Dense(units=128, activation='relu'))
    model.add(Dropout(0.2))
    
    model.add(Dense(units=256, activation='relu'))
    model.add(Dropout(0.2))
    
    # camada de saída utilizando softmax
    model.add(Dense(units=len(img_amt_class), activation='softmax'))

# compila
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary()

# inicializa a contagem de tempo
start_time = t.perf_counter_ns()

# treina
model.fit(x_train, y_train,
          batch_size = BATCH_SIZE, epochs = EPOCHS,
          validation_data=(x_test, y_test))

# finaliza a contagem de tempo
end_time = t.perf_counter_ns()


# SALVANDO DADOS -------------------------------------------------------------

save_path = 'model'
if DEBUG:
    save_path += '_debug'

# model
model_json = model.to_json()
with open("{}/model.json".format(save_path), "w") as json_file:
    json_file.write(model_json)

# weights
model.save_weights("{}/model.h5".format(save_path))

# meta
model_eval = model.evaluate(x_test, y_test)
meta = {
    "loss":model_eval[0],
    "accuracy":"{}%".format(model_eval[1]*100),
    "class_indices": data_dir_list,
    "duration": end_time - start_time,
    "end_timestamp": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "model_config": {
        "img_size": IMG_SIZE,
        "num_channels": NUM_CHANNELS,
        "batch_size": BATCH_SIZE,
        "epochs": EPOCHS,
    }
}

with open('{}/meta.json'.format(save_path), 'w') as json_file:
    json.dump(meta, json_file, indent=4)


def find_class(res):
    i = 0
    index = 0
    big = res[0][0]
    for i in range(len(res[0])):
        if res[0][i] > big:
            index = i
            big = res[0][i]
    return data_dir_list[index]


res_percent = [0]
res_predict = [[]]
cur_class = 0
i = 0
test_amt = []

for iac in range(len(img_amt_class)):
    test_amt.append(img_amt_class[iac] * 0.25)

for img in x_test:
    img = np.expand_dims(img, axis=0)
    finded_index = model.predict(img)
    finded_class = find_class(finded_index)
    res_predict[-1].append(finded_class)
    if data_dir_list[cur_class] == finded_class:
        res_percent[-1] += 100 / test_amt[cur_class]
    i += 1
    if i >= test_amt[cur_class]:
        i = 0
        cur_class += 1
        res_predict.append([])
        res_percent.append(0)

res_percent.pop()
res_predict.pop()

# printa e salva os resultados
#print('Result %: {}.'.format(res_percent))
#print('Result predicted: {}.'.format(res_predict))

full_res = {
    "shape":img_data.shape,
    "class indices":data_dir_list,
    "num of images by class":img_amt_class,
    "results %":res_percent,
    "predicted results":res_predict
}

print(full_res)

with open('{}/train_test_results.json'.format(save_path), 'w') as json_file:
    json.dump(full_res, json_file, indent=4)
