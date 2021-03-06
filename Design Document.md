
# VAEGAN

## Contributors
+ Conor OBrien
+ Jay Singh
+ Shakuntala Mitra
+ Shon Inouye

## Table of Contents
+ Step 1: Get data
+ Step 2: Neural Networks...?
+ Step 3: ???
+ Step 4: Profit

## Abstract
VAEGANs Unite!
Our project's goal is to be able to generate new video footage from existing videos.

[VAE Explained](http://kvfrans.com/variational-autoencoders-explained/)

## General Plan
+ Code Analysis / Read thru of existing MNIST model
+ Extend Code to three dimensions: B&W --> RGB
+ Convert to MNIST format

Update:
+ Convert B&W image into MNIST format

## 7/27/2017
Accomplished today:
+ Set up everyone to work with Python on their machine
+ Refresh knowledge of adversarial neural networks (ANN) and VAE technique
+ Look through existing MNIST code and run training program on Jupyter

Next steps:
+ Make sure everyone is able to comfortably manipulate MNIST model by next week
    + Understand what each piece of code is doing!
+ Continue reviewing VAE concepts
+ Develop tangible goals and timeline for this project

## 8/3/2017
Accomplished today:
+ Ran VAE number replication project from Conor's github
+ Researched MNIST and determined future steps for recreating other images

Next steps:
+ Continue researching concepts (VAE, GAN, MNIST, etc.)
+ Figure out how to convert images to MNIST format
+ Run model with new image

## 8/8/2017
Accomplished today:
+ Brainstormed ideas for adapting MNIST model to RGB (1 channel to 3 channels)
    + Discussed compression techniques (ex. Lossy, Hilbert curves, etc.)
    + Increasing the number of adversarial networks?
+ Discussing image continuity
+ Refining our project idea
    + Is the original project code transferable?
    + Generate new footage from old footage without accounting for temporal continuation
+ Chose a starting video/gif for our training set

Next steps:
+ Continue researching concepts (VAE, GAN, MNIST, etc.)
+ Figure out how to convert images to MNIST format
+ Find similar video processing projects as examples
+ Write up a simple model skeleton in Python

## 8/10/2017
Accomplished today:
+ Redefined our project goals:
    + Reconstruct an original image that is in the art style of *Rick and Morty* using MNIST
    + Possible future steps from here: Generate more images, order them into a short video clip (like a trailer)
+ Researched MNIST and other machine learning, image classification, and image generation techniques

Next steps:
+ Move away from using MNIST model and continue researching other generative techniques and how to manipulate them
+ Download frames from *Rick and Morty* TV episodes and create training and test datasets
+ Figure out how to convert images to MNIST format, either using original code or third-party software
+ Start building our generative model in Python using Tensorflow

## 8/17/2017
Accomplished today:
+ Take steps to make an image classifier for Rick and Morty images
+ Explore more about Docker

Next steps:
+ Run tensorflow classification project (https://www.youtube.com/watch?v=QfNvhPx5Px8&feature=youtu.be)
+ Read documentation on different classification algorithms (KNN, Random Forests, Decision Trees, SVM, etc.)
+ Create README.md

## 8/24/2017
Accomplished today:
+ Made a README.md
+ Learn how to split and label training data
+ Intro to k-NN

Next steps:
+ Read documentation on k-NN
+ Create labels for training data set
    + Go through frames, split into 2 folders (pictures with Rick and pictures w/o Rick), upload to Slack group
+ Figure out Google Image Search API to be able to pull images for testing our model

## 8/31/2017
Accomplished this week:
+ Separated the data and labelled it
+ Started building k-NN classifier for Morty

Next steps:
+ Have a working implementation of k-NN
+ "Clean the data"
    + Load all necessary Python packages
    + Read in the data
    + Prep images for feature extraction (aka turn them into vectors)
    + Split into test and training data sets

## 9/7/2017
Accomplished today:
+ Installed the necessary Python packages to run the k-NN model
+ Started running code

Next steps:
+ Everyone try to train the model
+ Update GitHub and Inertia7 w/ working code

## 9/14/2017
Accomplished today:
+ Ran KNN model on Rick and Morty images and got >90% accuracy

Next steps:
+ Update GitHub and Intertia7 w/ working code
+ Train on more images
+ Show misclassified images
+ Research other models 

## 9/27/2017
Accomplished today:
+ Run k-NN classifier w/ images in greyscale, compare accuracy to test with the RGB images
+ Start looking into SVM and Random Forest

Next steps:
+ Investigate the greyscale k-NN results
+ Update GitHub and Inertia7 w/ working code
+ Train on more images
+ Investigate SVM and Random Forest algorithms

## 10/26/2017 : Project progress resumed
