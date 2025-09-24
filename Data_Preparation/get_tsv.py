from pathlib import Path


# Base directory of the project
base_dir = Path("LB2_project_Group_5/Data_Preparation")

# Input and output paths for positive dataset
positive_ids = base_dir / "Positive_Cluster" / "rep_positive.ids"
pos_cluster_file = base_dir / "Positive_Cluster" / "pos_cluster-results_cluster.tsv"
pos_out_file = base_dir / "Positive_Cluster" / "pos_cluster_results.tsv"

# Input and output paths for negative dataset
negative_ids = base_dir / "Negative_Cluster" / "rep_negative.ids"
neg_cluster_file = base_dir / "Negative_Cluster" / "neg_cluster-results_cluster.tsv"
neg_out_file = base_dir / "Negative_Cluster" / "neg_cluster_results.tsv"


def write_tsv(file_input, file_input_cluster, file_output):
    with open(file_output, "w") as write:
        with open(file_input, "r") as ids:
            for i in ids:
                i = i.rstrip()
                with open(file_input_cluster, "r") as tsv:
                    for line in tsv:
                        if i in line:
                            print(line.rstrip(), file=write)
                            break

if __name__ == "__main__":
    try:
        write_tsv(positive_ids,pos_cluster_file,pos_out_file)
        print("Positive dataset filtered and saved to", pos_out_file)
        write_tsv(negative_ids,neg_cluster_file,neg_out_file)
        print("Negative dataset filtered and saved to", neg_out_file)
    except Exception as e:
        print(e)


