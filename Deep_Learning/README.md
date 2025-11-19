# LAB2 Project – Deep Learning
This section describes the deep learning approach implemented to classify protein sequences as signal peptide (SP) positive or negative using a Multi-Layer Perceptron (MLP) trained on high-dimensional embeddings extracted from the ESM-2 (T33_650M) protein language model.

The purpose of this module is to extend the classical methods (von Heijne, SVM) by introducing a feature-rich, data-driven model capable of learning complex sequence patterns through state-of-the-art protein representations.

| Method | Type | Implementation |
|---------|------|----------------|
| **ESM-2 + MLP** | Deep Learning | Transformer-based Embeddings + Multi-Layer Perceptron |

**Notebook:** `DL_analysis.ipynb`

---

## **Objective**
The goal is to build a robust classifier for signal peptide prediction by leveraging Transfer Learning and automated optimization. Rather than relying on manual feature engineering, this approach uses:

- **Pre-trained Embeddings:** Leveraging ESM-2 to capture evolutionary and structural context without explicit feature calculation.
- **Data-Driven Classification:** Training a neural network tailored to detect complex, non-linear patterns in the sequence data.
- **Rigorous Optimization:** Using Optuna for hyperparameter tuning and Cross-Validation to ensure generalization.


---

## Workflow Summary

| Step | Description |
|------|--------------|
| **1. Dataset Preparation** | Custom split into `train_sp.fasta` (folds 1-3), `val_sp.fasta` (folds 4-5), and `test_sp.fasta` |
| **2. Embedding** | Sequence encoding using `facebook/esm2_t33_650M_UR50D` (1280-d), sliced to the first **90 AA** |
| **3. Optimization**  | **Optuna** study (10 trials) to tune hidden layers, dropout rates, and learning rate |
| **4. Training**      | Training with **CrossEntropyLoss**, **Adam** optimizer, and **Early Stopping** |
| **5. Evaluation** | Final performance assessment on the independent blind test set |

---

## Model Architecture and Optimization

### (a) Network Structure
The classifier is a **Multi-Layer Perceptron (MLP)** designed for robustness:
* **Input (N-Terminal Focus:** 1280-dimensional semantic vectors (ESM-2 output) extracted from the first 90 residues only, reducing noise from the rest of the protein.
* **Global Pooling:** Averages the token embeddings to produce a fixed-size representation.
* **Hidden Layers:** Three dense layers with **ReLU** activation to model non-linear decision boundaries.
* **Regularization:** **Dropout** is applied after each layer to prevent the model from relying on specific neurons (overfitting).

### (b) Hyperparameter Tuning (Optuna)
An automated study identified the optimal configuration to maximize the Validation MCC:
| Hyperparameter | Optimal Value |
|----------------|---------------|
| **Hidden Size 1** | 45 |
| **Hidden Size 2** | 48 |
| **Hidden Size 3** | 41 |
| **Dropout Probability** | ~0.21 |
| **Learning Rate** | ~8e-4 |

---

## Training Performance

The training process incorporated **Early Stopping** (patience = 10 epochs) to ensure the selection of the model state with the best generalization capability.

* **Best Validation Score:** 0.9859 (MCC).
* **Convergence:** The model converged rapidly (epoch 19), confirming that the pre-trained ESM-2 features are highly discriminative for this task.

---

## Final Evaluation

The optimized model was evaluated on the independent **Test Set**.

| Metric | Score |
|--------|-------|
| **Matthews Corr. Coeff. (MCC)** | **0.9692** |

**Interpretation:**
- The Deep Learning approach achieves a high MCC of **0.9692**.
- The superior performance compared to classical methods confirms that **Transformer-based embeddings** effectively capture the complex, degenerate motifs of signal peptides.

---

## Output Files

| File | Description |
|------|--------------|
| `DL_bench_res.txt` | Final confusion matrix and detailed classification metrics |
| `train_sp.fasta` / `val_sp.fasta` | Custom FASTA splits generated for training and validation |
| `test_sp.fasta` | Independent dataset used for final benchmarking |
