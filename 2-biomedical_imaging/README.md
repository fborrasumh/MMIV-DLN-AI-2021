# Biomedical imaging in time and space

## Learning objectives

In the following series of seven Jupyter notebooks will explore **multichannel imaging data** from two quite different **imaging modalities** (in terms of physical principles and spatial resolution): 
- **Imaging Mass Cytometry** ([IMC](./IMC.md))
- **Magnetic Resonance Imaging** ([MRI](./MRI.md))

and illustrate the **generic nature of computational imaging**. <br>


More specifically:
- image processing, image noise, image filtering (e.g. Gabor filters) 
- supervised and unsupervised tissue classification in structural MRI (sMRI) recordings
- the nature of 4D (3D + time) resting state BOLD functional MRI (rs-fMRI)
- brain connectivity and graph representation towards Network science (being the next module in the course)


### Presentations: "Biomedical imaging in time and space"
- [[Part 1](https://docs.google.com/presentation/d/11U7L6OOP0M1bGZ-za0vy2dRqR8RJ3f07t4sjtvzkJpA/edit?usp=sharing)]
- [[Part 2](https://docs.google.com/presentation/d/1j8LGfbNyg9CvS0d6li2rfeJ9nnwGq_NZS2EWWcGGNe8/edit?usp=sharing)]

-------------------------

## Before you start on this module: 

### Install and configure the conda environment `mmiv-dln-img`:
```bash
conda env create -f environment-img.yml
```

### Activate the environment:
```bash
conda activate mmiv-dln-img
```

### Install the specific `MMIV-DLN-IMG` Jupyter kernel:
```bash
python -m ipykernel install --user --name mmiv-dln-img --display-name "MMIV-DLN-IMG"
```

## Update:
The code and environment can be updated during the course. Run the following commands regularly from within this directory:

* Update this particular `mmiv-dln-img` environment:
```bash
conda activate mmiv-dln-img
conda env update --file environment-img.yml
```
-------------------------

# The series of notebooks:

- [**IMG-Example-1-get-MRI-IMC-data.ipynb**](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/IMG-Example-1-get-MRI-IMC-data.ipynb) <a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/IMG-Example-1-get-MRI-IMC-data.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
 
- [**IMG-Example-2-imaging-intro.ipynb**](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/IMG-Example-2-imaging-intro.ipynb) <a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/IMG-Example-2-imaging-intro.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  
- [**IMG-Example-3-MRI-intro.ipynb**](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/IMG-Example-3-MRI-intro.ipynb) <a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/IMG-Example-3-MRI-intro.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  
- [**IMG-Example-4-IMC-intro.ipynb**](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/IMG-Example-4-IMC-intro.ipynb) <a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/IMG-Example-4-IMC-intro.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  
- [**IMG-Example-5-sMRI-KNN-tissue-classification.ipynb**](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/IMG-Example-5-sMRI-KNN-tissue-classification.ipynb) <a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/IMG-Example-5-sMRI-KNN-tissue-classification.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>

- [**IMG-Example-6-sMRI-Kmeans-tissue-classification.ipynb**](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/IMG-Example-6-sMRI-Kmeans-tissue-classification.ipynb) <a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/IMG-Example-6-sMRI-Kmeans-tissue-classification.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  
- [**IMG-Example-7-fMRI-resting-state.ipynb**](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/IMG-Example-7-fMRI-resting-state.ipynb) <a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/IMG-Example-7-fMRI-resting-state.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  
-------------------------

#### In your spare time - relax and enjoy biological vision:
See [this webpage](https://michaelbach.de/ot) containing demos of many beautiful and fascinating optical illusions and visual phenomena. Michael Bach gives detailed descriptions of these phenomena also from a theoretical perspective.<br>
Even more interested? see https://foundationsofvision.stanford.edu by Brian A. Wandell at Stanford.


<!--

### Download the IMC and MRI data from Goggle Drive cloud: 

## [00-get-mri-imc-data.ipynb](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/00-get-mri-imc-data.ipynb)
<a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/00-get-mri-imc-data.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

```
2-biomedical_imaging % tree data

data
├── imc
│   ├── E08_a0_full.csv
│   ├── E08_a0_full.tiff
│   └── table1_IMC_panel_37x4.csv
└── mri
    ├── 0.0-test_nifti.nii.gz
    ├── BraTS20
    │   ├── BraTS20_Training_002_HDGlioSeg.nii.gz
    │   ├── BraTS20_Training_002_flair.nii.gz
    │   ├── BraTS20_Training_002_seg.nii.gz
    │   ├── BraTS20_Training_002_t1.nii.gz
    │   ├── BraTS20_Training_002_t1ce.nii.gz
    │   └── BraTS20_Training_002_t2.nii.gz
    ├── brain_roi_mask.nii.gz
    ├── dess_060.dcm
    ├── dess_060.nii.gz
    ├── fisp_060.dcm
    ├── fisp_060.nii.gz
    ├── flash_060.dcm
    ├── flash_060.nii.gz
    ├── flash_060_brain_mask.png
    ├── flash_060_training_mask_6cla.png
    ├── mni_icbm152_t1_tal_nlin_sym_09c.nii.gz
    ├── multispectral_mri_training_data.csv
    ├── psif_060.dcm
    ├── psif_060.nii.gz
    └── training_mask_1_6.nii.gz
```

## [01-imaging-intro.ipynb](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/01-imaging-intro.ipynb)
<a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/01-imaging-intro.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
(Wednesday May 12th)

In this notebook we will learn about general terms and concepts related to digital images and digital image processing, including some topics (Gabor filtering) relevant to biological vision (simple cells in V1) and convolutional neural networks (CNNs) will be demonstrated.<br>
We will also introduce Python-based tools (libraries) for reading image files of various image formats (e.g. PNG, DICOM, NIFTI).

**More specifically**, being able to answer:

  -  What is a digital image? pixel? voxel? image matrix?
  -  What is pixel density (PPI) and field of view (FOV)?
  -  Examples of signal intensity transformations (e.g. contrast stretching, intensity inversion, intensity thresholding, histogram equalization)
  -  What is a convolution? (give examples of convolution filtering, e.g. averaging, median, Gaussian blurring, Canny edge detection, Gabor filterbanks)
  -  What is mathematical morphology? (give some examples, e.g. dilation, erosion, opening, closing, edge detection, granulometry)
  -  What is a coordinate transformation? and image registration? (give examples: rigid, affine, curved, elastic / deformable)
  -  What is digital image restoration? (give some examples, e.g. correction of intensity inhomogeneity, noise reduction, deconvolution)
  -  What is colocalization in biological microscopy and cell imaging?
  -  What is volume rendering? and surface rendering?
  -  What is DICOM? and NIFTI?
  -  What is RGB in relation to color images? color composition? and color separation?
  -  Give examples of multi-channel images


## [02-imc-intro.ipynb]
(Wednesday May 12th)


## [03-mri-intro.ipynb]
(Wednesday May 12th)


## [04-mri-knn-tissue-classification.ipynb](https://nbviewer.jupyter.org/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical_imaging/04-mri-knn-tissue-classification.ipynb)
<a href="https://colab.research.google.com/github/MMIV-ML/MMIV-DLN-AI-2021/blob/master/2-biomedical-imaging/04-mri-knn-tissue-classification.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
(Friday May 14th)

- In this notebook you will learn to predict predefined tissue types in a given multispectral MR image using  machine learning (**supervised classification**)

- The supervised classification model we wil use is simple **K-nearest neighbor** classification model, denoted _f_ (described below)

- To perform such pixel-wise tissue classification we will make use of the training (i.e. the `training mask`) we obtained during the **labelling of data** (see figure below of color-coded tissue samples)

- In the previous data labeling step (not part of these notebooks) we defined six different classes (tissue types), denoted <img src="https://latex.codecogs.com/svg.image?\mathbf&space;y" title="\mathbf y" /> and the corresponding four channel multispectral MRI data, dentoted <img src="https://latex.codecogs.com/svg.image?\mathbf&space;X" title="\mathbf X" />. 

- The notebook is thus a practical machine learning example of the formalism: <img src="https://latex.codecogs.com/svg.image?y&space;\approx&space;f\left(\mathbf&space;X,&space;\theta\right)" title="y \approx f\left(\mathbf X, \theta\right)" /> (uses https://latex.codecogs.com)

- You will also learn to navigate and appreciate the distinction between **image space** (pixel locations, spatial neiborhoods) and **feature vector space** (signal intensity value combinations, and similarity of pixel-based and tissue-based "signatures").



## 05-mri-kmeans-tissue-classification.ipynb
(Friday May 14th)


## 06-imc-kmeans-tissue-classification.ipynb
(Friday May 14th)

-----------------

-->


