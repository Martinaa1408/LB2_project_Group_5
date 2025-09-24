# Create output folders
mkdir Positive_Cluster
mkdir Negative_Cluster
mkdir Cross_Validation


# Cluster positive and negative sets with MMseqs2 module
#   --min-seq-id 0.3 : sequences grouped if ≥30% identity
#   -c 0.4           : alignment must cover ≥40% of sequence
#   --cov-mode 0     : coverage checked on both query and target
#   --cluster-mode 1 : more stringent clustering
mmseqs easy-cluster Data_Collection/Positive_Set/positive.fasta Positive_Cluster/cluster-results tmp \
  --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1

mmseqs easy-cluster Data_Collection/Negative_Set/negative.fasta Negative_Cluster/cluster-results tmp \
  --min-seq-id 0.3 -c 0.4 --cov-mode 0 --cluster-mode 1


# Extract representative IDs (one per cluster)
grep ">" Positive_Cluster/cluster-results_rep_seq.fasta | tr -d ">" > Positive_Cluster/rep_positive.ids
grep ">" Negative_Cluster/cluster-results_rep_seq.fasta | tr -d ">" > Negative_Cluster/rep_negative.ids


# Filter cluster tables to keep only representatives
python get_tsv.py


# Split representatives into training (80%) and benchmark (20%)
# Training includes 5 CV folds; benchmark is held out for evaluation
python get_sets.py


# Verify counts
echo "Representative counts:"
wc -l Positive_Cluster/rep_positive.ids
wc -l Negative_Cluster/rep_negative.ids

echo "Train/benchmark split counts:"
wc -l Cross_Validation/*


# Inspect content of the sets
echo "Positive training (first 5 lines):"
head -n 5 Cross_Validation/pos_train.tsv

echo "Positive benchmark (first 5 lines):"
head -n 5 Cross_Validation/pos_bench.tsv

echo "Negative training (first 5 lines):"
head -n 5 Cross_Validation/neg_train.tsv

echo "Negative benchmark (first 5 lines):"
head -n 5 Cross_Validation/neg_bench.tsv

