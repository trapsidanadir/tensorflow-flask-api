import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from functools import lru_cache



@lru_cache()
def detect(file_name:str):

    model = ResNet50(weights='imagenet')

    graph = tf.get_default_graph()

    original = image.load_img(file_name,target_size=(224,224))

    numpy_image = image.img_to_array(original)

    image_batch = np.expand_dims(numpy_image,axis=0)

    preprocess = preprocess_input(image_batch,mode='caffe')

    with graph.as_default():
        prediction = model.predict(preprocess)
    
    recognition = [ (element[1],int(element[2]*100))  for element in decode_predictions(prediction,5)[0]]

    return recognition