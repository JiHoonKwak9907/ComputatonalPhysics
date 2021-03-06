from cgi import test
from pickletools import optimize
import tensorflow as tf
from tensorflow import keras


import numpy as np
import matplotlib.pyplot as plt


fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


class_name = ['T-shirt/top',
              'Trouser',
              'Pullover',
              'Dress',
              'Coat',
              'Sandal',
              'Shirt',
              'Sneaker',
              'Bag',
              'Ankle boot']


train_images = train_images / 255.0
test_images = test_images / 255.0


model = keras.Sequential(
  [
    keras.layers.Flatten(input_shape = (28,28)),
    keras.layers.Dense(128, activation = tf.nn.relu), 
    keras.layers.Dense(10, activation = tf.nn.softmax),
    
    ]
)


model.compile(
  optimizer = 'adam',
  loss = 'sparse_categorical_crossentropy',
  metrics = ['accuracy']
  )


model.fit ( train_images, train_labels, epochs = 10)


test_loss, test_acc = model.evaluate(test_images, test_labels)


print("Accuracy (test sample) = ", test_acc)



predictions = model.predict (test_images)


print ("Predict for [5908]-th image", predictions[5908])


print ("Max of prediction", np.argmax( predictions[5908] ))


print("True Answer = ", test_labels[5908])


plt.figure()
plt.imshow(test_images[5908])
plt.show()