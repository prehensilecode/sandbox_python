#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import gzip
import time
import random

import tensorflow as tf
from tensorflow import keras

### Source: https://www.tensorflow.org/tutorials/keras/classification

### This was tested using TensorFlow 2.4.1 on CPU-only, and on a single GPU

### TensorFlow automatically uses a GPU if available.
### NOTE To use more than one GPU, that needs to be configured with TensorFlow.
###      While TF may use a single GPU automatically, it will not automatically
###      distribute the computation to multiple GPUs.

def plot_image(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                    100*np.max(predictions_array),
                                    class_names[true_label]),
                                    color=color)


def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte.gz'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte.gz'
                               % kind)

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8,
                               offset=8)

    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8,
                               offset=16).reshape(len(labels), 784)

    return images, labels


# sanity check
print('')
print(f"TensorFlow version = {tf.__version__}")
print(f"Keras version = {keras.__version__}")
print('')

if tf.test.gpu_device_name():
    print('Connected to GPU(s)', tf.test.gpu_device_name())
else:
    print('Not connected to GPU')
print('')

# load data
#train_images, train_labels = load_mnist('/beegfs/Sample_TF_Datasets/Fashion_MNIST', kind='train')
#test_images, test_labels = load_mnist('/beegfs/Sample_TF_Datasets/Fashion_MNIST', kind='t10k')
train_images, train_labels = load_mnist('.', kind='train')
test_images, test_labels = load_mnist('.', kind='t10k')

# define class names
class_names = ('T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot')

print(f'train_images.shape = {train_images.shape}')
print(f'train_labels.shape = {train_labels.shape}')
print(f'test_images.shape = {test_images.shape}')
print(f'test_labels.shape = {test_labels.shape}')
print('')

# normalize images
train_images = train_images / 255.0
test_images = test_images / 255.0

# build model
# NOTE loaded data is already flattened, so we remove the Flatten() layer from the original tutorial
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
    ])

# compile model
model.compile(optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])

# train
print('Training starting...')
tic = time.perf_counter()
model.fit(train_images, train_labels, epochs=20)
toc = time.perf_counter()
print('')
print(f'Training completed in {toc - tic:0.4f} seconds')
print('')

# evaluate accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f'Test accuracy: {test_acc}')

probability_model = tf.keras.Sequential([model,
    tf.keras.layers.Softmax()])

# verify predictions
predictions = probability_model.predict(test_images)
print(f'predictions[0] = {predictions[0]}')
print(f'highest confidence label = {class_names[np.argmax(predictions[0])]}')
print(f'matching test label = {class_names[test_labels[0]]}')

# plot several test images, their predicted labels, and their true labels
test_images_reshaped = np.reshape(test_images, (test_images.shape[0], 28, 28))

num_rows = 5
num_cols = 3
num_images = num_rows * num_cols
fig = plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions[i], test_labels, test_images_reshaped)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions[i], test_labels)
    plt.tight_layout()

plt.savefig('verification.png', bbox_inches='tight')
plt.close(fig)


# use the trained model for prediction/inference
print('')
print('Make a prediction on a random image using the model we trained')

# pick an image from test dataset
print(f'There are {test_images.shape[0]} test images')
img_id = random.randint(0, test_images.shape[0])
print(f'Select image no. {img_id}')
img = test_images[img_id]
img_reshaped = np.reshape(img, (28, 28))
print(f'img_reshaped.shape = {img_reshaped.shape}')

# tf.keras models work on a batch of examples. Make a batch of one.
img = (np.expand_dims(img, 0))

predictions_single = probability_model.predict(img)
print(f'Prediction = {class_names[np.argmax(predictions_single[0])]}')

plt.grid(False)
fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(8)
plot_value_array(1, predictions_single[0], test_labels)
plt.subplot(num_rows, 2, 1)
plt.imshow(img_reshaped, cmap=plt.cm.binary)
plt.subplot(num_rows, 2, 2)
plot_value_array(0, predictions_single[0], test_labels)
plt.xticks(range(10), class_names, rotation=90)
plt.savefig('prediction.png', bbox_inches='tight')
plt.close(fig)
