# LAB2 Project – Deep Learning

This section describes the deep learning approach implemented to classify protein sequences as signal peptide (SP) positive or negative. The model extends classical methods by utilizing a **Multi-Layer Perceptron (MLP)** trained on high-dimensional embeddings from the **ESM-2 (T33_650M)** protein language model.

| Method | Type | Implementation |
|---------|------|----------------|
| **ESM-2 + MLP** | Deep Learning | Transformer-based Embeddings + Multi-Layer Perceptron |

**Notebook:** `DL_analysis.ipynb`

---

## **Objective & Approach**

The goal is to build a robust classifier for signal peptide prediction by leveraging **Transfer Learning** and automated optimization. Rather than relying on manual feature engineering, this approach uses:

* **Pre-trained Embeddings:** Leveraging **ESM-2** to capture evolutionary and structural context without explicit feature calculation.
* **Data-Driven Classification:** Training a neural network tailored to detect complex, non-linear patterns in the sequence data.
* **Rigorous Optimization:** Using **Optuna** for hyperparameter tuning and **Cross-Validation** to ensure generalization.

---

## Workflow Summary

| Step | Description |
|------|--------------|
| **1. Dataset Preparation** | Custom split into `train_sp.fasta` (folds 1-3), `val_sp.fasta` (folds 4-5), and `test_sp.fasta` |
| **2. Embedding** | Sequence encoding using `facebook/esm2_t33_650M_UR50D` (1280-d) |
| **3. Optimization** | **Optuna** study (10 trials) to tune hidden layers, dropout rates, and learning rate |
| **4. Training** | Training with **CrossEntropyLoss**, **Adam** optimizer, and **Early Stopping** |
| **5. Evaluation** | Final performance assessment on the independent blind test set |

---

## Model Architecture and Optimization

### Network Structure & Input Processing
The classifier is a **Multi-Layer Perceptron (MLP)** designed to focus on the biologically relevant N-terminal region.

* **Input (N-Terminal Focus):** 1280-dimensional ESM-2 vectors extracted from the **first 90 residues** only, reducing noise from the rest of the protein.
* **Global Pooling:** Averages the token embeddings to produce a fixed-size representation.
* **Hidden Layers:** Three dense layers with **ReLU** activation to model non-linear decision boundaries.
* **Regularization:** **Dropout** is applied after each layer to prevent overfitting.

### Hyperparameter Tuning (Optuna)
An automated study (Trial 7) identified the optimal configuration to maximize the Validation MCC:

| Hyperparameter | Optimal Value |
|----------------|---------------|
| **Hidden Size 1** | 45 |
| **Hidden Size 2** | 48 |
| **Hidden Size 3** | 41 |
| **Dropout Probability** | 0.21 |
| **Learning Rate** | 7.97e-4 |

---

## Training Performance

The training process incorporated **Early Stopping** (patience = 10 epochs) to ensure the selection of the model state with the best generalization capability.

* **Best Validation Score:** 0.9893 (MCC) achieved at Epoch 9.
* **Convergence:** The model converged rapidly, triggering early stopping at Epoch 19. This indicates that the pre-trained ESM-2 features are highly discriminative, requiring minimal gradient updates to separate the classes effectively.

---

## Final Evaluation

The optimized model was evaluated on the independent **Test Set** (2006 sequences).

| Metric | Score |
|--------|-------|
| **Accuracy** | 0.994 |
| **Precision** | 0.973 |
| **Recall** | 0.973 |
| **F1 Score** | 0.973 |
| **MCC** | **0.969** |

**Confusion Matrix:**


| | **Predicted Negative** | **Predicted Positive** |
| :--- | :---: | :---: |
| **Actual Negative** | 1781  | 6  |
| **Actual Positive** | 6  | 213  |


**Interpretation:**
The Deep Learning approach achieves a near-perfect classification with an MCC of **0.969**. The balanced errors (only 6 false positives and 6 false negatives) demonstrate that the model is unbiased and handles the class imbalance effectively.

---

## Output Files

| File | Description |
|------|--------------|
| [DL_bench_res_hyperparameter.txt](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Deep_Learning/DL_bench_res_hyperparameter.txt)| Final confusion matrix and detailed metrics of the Optimized Model on the Test Set |
| [DL_bench_res.txt](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Deep_Learning/DL_bench_res.txt) | Baseline model results (manual hyperparameters) on test set |
| [training_validation_loss.png](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Deep_Learning/Plots/training_validation_loss.png) | Plot of Training and Validation Loss curves over epochs |




