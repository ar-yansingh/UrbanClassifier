#  Urban Sound Classification using Deep Learning

This project implements an end-to-end Machine Learning pipeline to classify environmental sounds into 10 distinct categories using the **UrbanSound8K** dataset. By transforming raw audio into frequency-domain features (MFCCs), a Dense Artificial Neural Network (ANN) was trained to identify patterns across thousands of urban sound clips.

---

##  Dataset
The **UrbanSound8K** dataset contains 8,732 labeled sound excerpts (≤ 4s) of urban sounds from 10 classes:

* **Air Conditioner**, **Car Horn**, **Children Playing**, **Dog Bark**, **Drilling**, **Engine Idling**, **Gun Shot**, **Jackhammer**, **Siren**, and **Street Music**.

 [Dataset Link (Kaggle)](https://www.kaggle.com/datasets/chrisfilo/urbansound8k)

---

##  Tech Stack
* **Language:** Python 3.x
* **Audio Processing:** Librosa
* **Deep Learning:** TensorFlow / Keras
* **Data Science:** Pandas, NumPy, Scikit-learn
* **Visualization:** Matplotlib, Seaborn

---

##  Feature Engineering
Raw audio waveforms are difficult for standard ANNs to process. This project utilizes **Mel-Frequency Cepstral Coefficients (MFCCs)** to represent the "timbre" of the sound.

* **Extraction:** Extracted 40 MFCCs per audio sample.
* **Aggregation:** Calculated the mean of the MFCCs across the time axis to create a fixed-size 1D feature vector for each file.
* **Scaling:** Applied `StandardScaler` to normalize features, ensuring stable and faster model convergence.

---

##  Model Architecture
The project uses a Sequential **Artificial Neural Network (ANN)** designed to handle 1D feature inputs:

* **Input Layer:** 40 neurons (MFCC features).
* **Hidden Layers:** Three dense layers (256, 512, 256 neurons) using **ReLU** activation.
* **Regularization:** Dropout layers (0.3) to prevent overfitting.
* **Output Layer:** 10 neurons with **Softmax** activation for multi-class classification.
* **Training:** Optimized using the **Adam** optimizer and **Categorical Crossentropy** loss.

---

##  Performance
* **Validation Accuracy:** `92.22%`
* **Optimization:** Utilized **Early Stopping** to monitor validation loss and prevent overtraining.
