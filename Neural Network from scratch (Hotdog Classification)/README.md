# Neural Network from scratch

## Description
In this repo we will discuss how to create a Deep Neural Network from scratch to do an image classification task, specifically classifying hotdog images. The given data will be around 1000 images. Some of these images will be hotdog images, and the other are some other random images. 

In the end of this project, you will be able to understand:

- The basic functionality inside a neural network.
- The basic concepts inside neural network.
- Create your own deep neural network.

## Purpose
Understanding the inside architecture of neural networks is a major requirement to create modern and state-of-the-art applications. Most of the leading corporations like Google, Microsoft, apple, amazon ... etc. are have a huge dependency on deep learning algorithms. Huge projects like siri, Google Search, Microsoft Translate and others can't exist without deep learning models.

## Installation Guide
To be able to follow this project, you have to install only the **cv2** package which is a module for images manipulation. This module can be installed by running the following command:
`conda install -c menpo opencv3`


## Preprocessing
The first thing in any data science project is to engineer the data that you are going to use. This process is called **Preprocessing** and that's becuase it's the process before processing the data into a certain model. To preprocess our data you can use the `preprocessing.ipynb` file. All this file is doing is to turn all the hotdog images into a hdf5 files. These hdf5 will be used in the following process.


## Training
This process is the process where we create a deep learning model that can solve our problem. To create a deep neural network model and train it, you can run the `train.ipynb` file.


## Try It Yourself
After creating a model, now it's time to use it to classify an image of your own. You can do that by running the `running.ipynb` file. This file uses the file `model.pickle` to load the parameters fo the model and use it on predicting the input image.
