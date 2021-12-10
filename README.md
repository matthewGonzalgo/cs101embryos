# CS101 Embryos
### Introduction
This code repository contains code for the 2021 fall CS101 embryo project.



### Usage
#### Image Classification
1. Download the Z-stack Dataset created to be used with the Vision Transformer model.
2. Run the "./classification/embryo_classification.ipynb" notebook. \
 **Note**: Some modifications to the ViT utility code this notebook utilizes may need to be made in order for some parts of the notebook to run. These potential changes are noted in the notebook.

#### Boundary Detection
1. Download the individual Z-stack slice dataset and trained weights.
2. Run the "./boundary_detection/boundary_detection.ipynb".

#### Object Detection
1. Download the compressed Z-stack dataset and trained weights.
2. Run the "./object_detection/object_detection.ipynb" notebook.

#### Segmentation
For z-stack slice segmentation:
1. Download the individual Z-stack dataset and trained weights
2. Run the "./segmentation/single_slice/dic/single_slice_dic_segmentation.ipynb" notebook.

For 3D Z-stack segmentation:
1. Download the 32-channel Z-stack dataset and trained weights
2. Run the "./segmentation/3d/3d_segmentation.ipynb" notebook.


### Datasets
1. [Individual Z-stack slice Dataset](https://drive.google.com/file/d/1jreUNIDvlbYAdH1_KjD8Y351ef2gqhfK/view?usp=sharing)
2. [Compressed Z-stack Dataset](https://drive.google.com/file/d/16JBoZ8piIcysOjgbbKOf1IW7tnnKEq2h/view?usp=sharing)
3. [Compressed Z-stack Dataset for use with Vision Transformer model](https://drive.google.com/file/d/1HuyJOEOhkXC8LmyGaBi3jjaUWWlshLZB/view?usp=sharing)
4. [32-channel Z-stack Dataset](https://drive.google.com/file/d/1laYvevrZK6duS5tR9IaSfeljOf8QE1oc/view?usp=sharing)


### Trained Weights
1. [Boundary Detection](https://drive.google.com/file/d/1bxuOCC1MtYNJyRb03QqftIafGOMArEHb/view?usp=sharing)
2. [Object Detection(compressed DIC)](https://drive.google.com/file/d/1B_knaMJ5pWx6WSwICc913PmQRpV1r8hz/view?usp=sharing)
3. [Object Detection(compressed fluorescence)](https://drive.google.com/file/d/10MnrDE7oYHhEA4RLaaSm0X64f0qOVQi1/view?usp=sharing)
4. [Segmentation on single-slice DIC](https://drive.google.com/file/d/1--PeQy3X3h3fQbM_eXjil9OUREXS4ZqQ/view?usp=sharing)
5. [Segmentation on single-slice Fluoresence](https://drive.google.com/file/d/1-Zj8FGxq3J7Cgwto2TMIopxf6faj4pom/view?usp=sharing)
6. [Segmentation on 3D DIC](https://drive.google.com/file/d/1-s3ZtMteQN720_FDZOqxbodKs1u9zMMQ/view?usp=sharing)
