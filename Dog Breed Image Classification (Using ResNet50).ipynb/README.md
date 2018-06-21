# Dog Breed Classification

## Description
Here, we are going to use a pre-trained Convolution Neural Network model called "ResNet50" which is a 50 layer Deep Convolution Neural Network. There are other variants like ResNet101 and ResNet152 also which consist of 101 layers and 152 layers respectively. This operation is knows as "Transfer Learning" where you take a model which does a certain task perfectly, then use that model to train on similar data.

If you want further deeper understanding of ResNets, you have to read this paper.... All my description above is by reading this paper only. Figure 2 of the paper shows the basic building block of residual network. If you want to see the ResNet-50 architecture in detail, this is the best page. I use this page very often. Netscope. You can hover over each block, to get more details about the block.

## Purpose
Understanding how to use famous neural network is a major requirement to create modern and state-of-the-art applications. Most of the leading corporations like Google, Microsoft, apple, amazon ... etc. are have a huge dependency on deep learning algorithms. Huge projects like siri, Google Search, Microsoft Translate and others can't exist without deep learning models.

## Installation Guide
To be able to follow this project, you have to install the following packages:
1. **cv2** package: which is a module for images manipulation. This module can be installed by running the following command:
`conda install -c menpo opencv3`
2. **Keras & Tensorflow**: Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow. You can install both Keras and Tensorflow by running these commands one at a time:
`conda install -c conda-forge keras` and `conda install -c conda-forge tensorflow `


## script
The given notebook is using the model `bestmodel.hdf5` to classify a given image of a dog and gets its breed.
