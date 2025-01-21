import tensorflow as tf;
from keras import models;
import numpy as np;
import sys;

json_file = open("./BUFFER_model.json", 'r');
loaded_model_json = json_file.read();
json_file.close();

loaded_model = models.model_from_json(loaded_model_json);

loaded_model.load_weights("./BUFFER_model.weights.h5");

print("Modelo cargado");

loaded_model.compile(loss='mean_squared_error',
                     optimizer='adam', metrics=['binary_accuracy']);

data = [int(sys.argv[1])];

data = np.array([data], "float32");

pre = loaded_model.predict(data).round();

print(int(pre[0][0]));