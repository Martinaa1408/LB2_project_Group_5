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

# File with extra info
info_file_pos = "LB2_project_Group_5/Data_Collection/Positive Set/positive.tsv"
info_file_neg = "LB2_project_Group_5/Data_Collection/Negative Set/negative.tsv"


def split_dataset(input_file, train_file, bench_file, label, info_file):
    """
    Split a dataset into training and benchmarking sets, adding extra info.
    Keep only seq_id present in the input file.
    """

    # Load dataset (1 column: seq_id)
    df = pd.read_csv(input_file, sep="\t", header=None, names=["seq_id"])
    df["seq_id"] = df["seq_id"].str.strip()   
    df["class"] = label
  

    # Load extra info
    info_df = pd.read_csv(info_file, sep="\t")
    info_df = info_df.rename(columns={"Accession": "seq_id"})  
    info_df["seq_id"] = info_df["seq_id"].str.strip()  
    
    # Merge only seq_id present in input_file
    df = df.merge(info_df, on="seq_id", how="inner")

    # Train/test split (80/20)
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
    split_dataset(pos_input, pos_train, pos_bench, "positive", info_file_pos)

    # Negative dataset
    split_dataset(neg_input, neg_train, neg_bench, "negative", info_file_neg)

