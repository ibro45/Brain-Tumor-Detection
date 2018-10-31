# Brain Tumor Detection

## Description
Our project aims to give ideas and possible solutions for detecting abnormalities in CT scans of brain. The goal is to have a system which would make accidental tumor findings possible in an autonomous way. What it means is that the system would provide assistance to the radiologist by indicating that a tumor is present on a CT scan taken for some other reason.

This project is done at the JunctionX Budapest 48-hour hackathon and is our approach to the challenge given by Varian, which can be found [here](https://budapest.hackjunction.com/challenges/varian).

A raw, unlabelled, dataset of CT and MR dicom images for 30 patients was provided.
After examining the challenge, we decided to go with two approaches for the problem:

1. Deep Learning Approach
2. Brain Symmetry Approach

## Deep Learning Approach

For supervised learning, labelled data is a requirement. Since the provided data wasn't labelled, we came up with a method to properly label it. For each series of scans, there is a file which indicates and contours the tumor(s) at each slice where it is located. We, therefore, decided to use that information to label each of the slices as either containing tumor or not containg tumor depending if a tumor is present there.

The next step was to decide on the model architecture. As we didn't have time to dive deep into this problem, we decided to go with VGG16 pretrained on Imagenet. Unfortunately, as expected, the model overfits on our dataset due to it's small quantity and uneven distribution (with there being more slices not containing any tumors than those that do). The second issue can be easily solved if the first issue's solved, which is something we are looking to solve in the near future.

## Brain Symmetry Approach

Given very limited amount of data we decided to take advantage of the natural symmetry of the right and left brain hemisphere. Healthy brains exhibit high correlation between hemispheres (over 0.9, see the figure below), whereas a potential brain tumor breaks this symmetry. This approach requires perfect orientation of the brain, meaning no rotation in either of the axis and the middle line cuts the brain to two hemispheres. We search this orientation with a random walk over different orientations and middle lines to maximise the slice symmetry.

Slices around the middle (of the vertical axis) with correlations 0.8 to 0.9 are more likely to contain tumor. Slices around the edges (the top of the brain, and the bottom) contains very little part of brain or bones which yields very low and unpredictable correlations and thus the tumor cannot be detected in this regions with the symmetry technique.

![Brain correlation distribution](https://raw.githubusercontent.com/ibro45/Brain-Tumor-Detection/master/Brain%20Symmetry%20Approach/corr_dist_brain.png)
