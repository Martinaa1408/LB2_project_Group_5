# Create directories to contain clusters of both positive and negative sets

mkdir Positive_Cluster
mkdir Negative_Cluster

# Create clusters of Positive
mmseqs easy-cluster LB2_project_Group_5/Data_Collection/Positive_Set/positive.fasta cluster-results
 tmp --min-seq-id 0.3 \-c 0.4 --cov-mode 0 --cluster-mode 1

# Create clusters of Negative
mmseqs easy-cluster LB2_project_Group_5/Data_Collection/Negative_Set/negative.fasta cluster-results
 tmp --min-seq-id 0.3 \-c 0.4 --cov-mode 0 --cluster-mode 1

# Count the numbers of representative sequences in the .fasta output

# Positive
grep ">" Positive_Cluster/cluster-results_rep_seq.fasta | wc

# Negative
grep ">" Negative_Cluster/cluster-results_rep_seq.fasta | wc
