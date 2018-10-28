# VarianBudapestJunction

## Brain Symmetry Approach

Given very limited amount of data we decided to take advantage of the natural symmetry of the right and left brain hemisphere. Healthy brains exhibit high correlation between hemispheres (over 0.9, see the figure below), whereas a potential brain tumor breaks this symmetry. This approach requires perfect orientation of the brain, meaning no rotation in either of the axis and the middle line cuts the brain to two hemispheres. We search this orientation with a random walk over different orientations and middle lines to maximise the slice symmetry.

Slices around the middle (of the vertical axis) with correlations 0.8 to 0.9 are more likely to contain tumor. Slices around the edges (the top of the brain, and the bottom) contains very little part of brain or bones which yields very low and unpredictable correlations and thus the tumor cannot be detected in this regions with the symmetry technique.

![Brain correlation distribution](https://raw.githubusercontent.com/ibro45/Brain-Tumor-Detection/master/Brain%20Symmetry%20Approach/corr_dist_brain.png)
