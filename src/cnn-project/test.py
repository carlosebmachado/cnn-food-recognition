from keras.models import model_from_json
import os
import cv2
import numpy as np
from keras_preprocessing import image
#import numpy as np
import json


# desabilita a notação ciêntifica
np.set_printoptions(precision=5, suppress=True)

# carrega os dados da construção do modelo
with open('model/meta.json', 'r') as json_file:
    meta = json.load(json_file)


# constants
BIG_TEST = True
COLOR = 3
GRAY = 1

IMG_SIZE = meta['model_config']['img_size']
NUM_CHANNELS = meta['model_config']['num_channels']

class_indices = meta['class_indices']


#carrega o modelo
json_file = open('model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('model/model.h5')


def find_class(res):
    i = 0
    index = 0
    big = res[0][0]
    for i in range(len(res[0])):
        if res[0][i] > big:
            index = i
            big = res[0][i]
    return class_indices[index]


if BIG_TEST:
    # TESTAR EM LOTES ------------------------------------------------------------
    
    # pega o diretório de trabalho atual
    PATH = os.getcwd()
    # define o caminho do dataset
    data_path = PATH + '/dataset/test_images'
    # pega a lista de classes
    data_dir_list = os.listdir(data_path)
    
    # quantidade de imagens em cada classe
    img_amt_class = []
    
    # loop para garregamento das imagens
    img_data_list = []
    for dataset in data_dir_list:
        img_list = os.listdir(data_path+'/'+ dataset)
        # adiciona um novo contador
        img_amt_class.append(0)
        print ('Loading images of {} class.'.format(dataset))
        for img in img_list:
            # contabiliza a img
            img_amt_class[-1] += 1
            # carrega, redimensiona e add
            input_img = cv2.imread(data_path + '/'+ dataset + '/'+ img )
            if NUM_CHANNELS == 1:
                input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
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
    
    res_percent = [0]
    res_predict = [[]]
    cur_class = 0
    i = 0
    for img in img_data:
        img = np.expand_dims(img, axis=0)
        finded_class = find_class(model.predict(img))
        res_predict[-1].append(finded_class)
        if class_indices[cur_class] == finded_class:
            res_percent[-1] += 10
        i += 1
        if i >= img_amt_class[cur_class]:
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
    
    with open('model/test_results.json', 'w') as json_file:
        json.dump(full_res, json_file, indent=4)

else:
    # TESTAR UMA -------------------------------------------------------------
    path = ''
    test_img = image.load_img(path, target_size=(IMG_SIZE,IMG_SIZE))
    
    test_img = image.img_to_array(test_img)
    test_img /= 255
    test_img = np.expand_dims(test_img, axis=0)
    result = model.predict(test_img)
    print('Resposta: ', find_class(result))
