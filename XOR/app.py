import os;
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0';
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1';
import tensorflow as tf;
import numpy as np;
from keras import models, layers;
import sys;

json_file = open('./model.json', 'r');
loaded_model_json = json_file.read();
json_file.close();
loaded_model = tf.keras.models.model_from_json(loaded_model_json);

loaded_model.load_weights('./model.weights.h5');
print('loaded model');

loaded_model.compile(loss='mean_squared_error',
                     optimizer='adam', metrics=['binary_accuracy']);

print('modelo compilado')

# Testar o modelo

data = [int(sys.argv[1]), int(sys.argv[2])];
data = np.array([data], "float32");

pre = loaded_model.predict(data).round();

print(int(pre[0][0]));