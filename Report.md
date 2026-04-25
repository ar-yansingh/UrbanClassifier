

**Author:** Aryan Singh

**Date:** January 2026

## 1. Project Objective

The goal of this project was to develop a deep learning model capable of classifying environmental sounds from the **UrbanSound8K** dataset. The focus was on understanding signal processing and implementing an Artificial Neural Network (ANN) to handle audio feature vectors.

## 2. Dataset Analysis

* **Source:** UrbanSound8K dataset.
* **Size:** 8,732 audio clips.
* **Classes:** 10 (Siren, Dog Bark, Drilling, etc.).
* **Observation:** The dataset is split into 10 folds to facilitate cross-validation. For this project, a standard 80/20 train-test split was used.

## 3. Methodology & Feature Engineering

Raw audio cannot be fed directly into an ANN. The following signal processing steps were taken:

* **Feature Extraction:** Used **MFCC (Mel-Frequency Cepstral Coefficients)** to capture the spectral characteristics of the sounds.
* **Dimensionality Reduction:** Extracted 40 MFCCs and calculated their **mean** across time to create a fixed-size 1D input (40 features).
* **Preprocessing:** Implemented `StandardScaler` to normalize the feature range, ensuring the model's weights converge effectively during training.

## 4. Model Architecture (ANN)

A **Sequential Artificial Neural Network** was designed with the following hyperparameters:

* **Layers:** 3 Hidden Layers (256  512  256 neurons).
* **Activations:** **ReLU** for hidden layers; **Softmax** for the output layer.
* **Regularization:** **Dropout (0.3)** to prevent overfitting by randomly deactivating neurons during training.
* **Optimization:** Used the **Adam** optimizer with **Categorical Crossentropy** loss.

## 5. Results and Discussion

* **Final Accuracy:** 92.22%
* **Key Findings:** The model performed exceptionally well on sounds with distinct frequency patterns like "Gun Shot" and "Siren."
* **Challenges:** Some confusion was noted between "Drilling" and "Jackhammer" due to their similar mechanical frequency signatures.

## 6. Conclusion and Future Work

This project successfully demonstrated the effectiveness of ANNs for 1D audio feature classification. Future improvements could include:

* Using **Data Augmentation** (pitch shifting/noise addition) to increase dataset diversity.
* Implementing a **CNN (Convolutional Neural Network)** to process 2D Mel-Spectrograms instead of 1D means.
