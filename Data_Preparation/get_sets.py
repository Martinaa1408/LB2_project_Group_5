#!/usr/bin/env python3
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# Base project folder
base_dir = Path("LB2_project_Group_5/Data_Preparation")

# Positive dataset paths
pos_input = base_dir / "Positive_Cluster" / "rep_positive.ids"
pos_train = base_dir / "Cross_Validation" / "pos_train.tsv"
pos_bench = base_dir / "Cross_Validation" / "pos_bench.tsv"

# Negative dataset paths
neg_input = base_dir / "Negative_Cluster" / "rep_negative.ids"
neg_train = base_dir / "Cross_Validation" / "neg_train.tsv"
neg_bench = base_dir / "Cross_Validation" / "neg_bench.tsv"


def split_dataset(input_file, train_file, bench_file, label):
    """
    Split a dataset into:
      - 80% training set
      - 20% benchmarking set
    Assign folds to the training set in a simple round-robin cycle (1–5).

    Parameters
    ----------
    input_file : Path
        Representative dataset in TSV format (seq_id, rep_id).
    train_file : Path
        Output training set with folds.
    bench_file : Path
        Output benchmarking set.
    label : str
        Class label ("positive" or "negative").
    """

    # Load dataset (2 columns: seq_id, rep_id)
    df = pd.read_csv(input_file, sep="\t", header=None, names=["seq_id"])
    df["class"] = label

    # Train/test split (80/20), reproducible with random_state
    train, bench = train_test_split(df, test_size=0.2, random_state=42)

    # Assign folds in round-robin order
    train = train.reset_index(drop=True)
    train["fold"] = [(i % 5) + 1 for i in range(len(train))]

    # Save results
    train.to_csv(train_file, sep="\t", index=False)
    bench.to_csv(bench_file, sep="\t", index=False)

    print("Processed:", input_file.name)
    print("Training set:", len(train), "sequences →", train_file)
    print("Benchmark set:", len(bench), "sequences →", bench_file)


if __name__ == "__main__":
    # Positive dataset
    split_dataset(pos_input, pos_train, pos_bench, "positive")

    # Negative dataset
    split_dataset(neg_input, neg_train, neg_bench, "negative")

