# LAB2_project — SVM Method 

This directory contains the **Support Vector Machine (SVM)** module of the LB2 *Signal Peptide Prediction* project.  
It represents the **classification and model optimization stage**, trained on the numerical features produced in the **Feature Extraction & Selection** phase.

The purpose is to develop and validate a binary model capable of distinguishing **signal peptide (SP)** sequences from **non-SP** proteins through **kernel-based learning**.

---

## Concept
The SVM algorithm constructs an optimal **hyperplane** that separates the two classes in a high-dimensional feature space.  
In this project, features correspond to compositional and physicochemical descriptors of protein N-terminal regions.

If the data are not linearly separable, the **kernel trick** maps them into a higher-dimensional space where separation is possible.  
The final classifier is a **maximum-margin separator** determined only by the **support vectors**.

---

## Workflow Summary
| Step | Description | Output |
|------|--------------|---------|
| **1. Input loading** | Import the feature matrix `ML_features.tsv` from the Feature Extraction phase. | DataFrame with numerical features and labels |
| **2. Preprocessing** | Normalize all variables using `MinMaxScaler`. Optionally recompute the 22-aa composition baseline. | Scaled feature matrix |
| **3. Model definition** | Initialize an SVM classifier (`sklearn.svm.SVC`). | SVM model |
| **4. Hyperparameter optimization** | Grid search with stratified 5-fold cross-validation. | Best-performing kernel and parameters |
| **5. Evaluation** | Compute metrics: Accuracy, Precision, Recall, F1, MCC. | Performance summary |
| **6. Feature selection (optional)** | Apply RandomForest importance or RFE for dimensionality reduction. | Reduced feature set |
| **7. Model saving** | Export trained SVM model and fitted scaler. | `.pkl` files |

---

