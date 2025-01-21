import tensorflow as tf;
from keras import models;
import sys;
import numpy as np;

json_file = open("./NOT_model.json", 'r');

loaded_model_json = json_file.read();

json_file.close();

loaded_model = models.model_from_json(loaded_model_json);

loaded_model.load_weights("./NOT_model.weights.h5");

print("Modelo carregado");

loaded_model.compile(loss='binary_crossentropy',
                   optimizer='adam');

data = [int(sys.argv[1])];

data = np.array([data], "float32");

result = loaded_model.predict(data);

print(int(result.round()));