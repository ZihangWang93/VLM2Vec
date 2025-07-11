from datasets import load_dataset, Dataset
from collections import defaultdict
import os
from tqdm import tqdm

# Output directory
output_dir = "/mnt/disks/embedding/data/vlm2vec/MMEB-train/visdoc/vidore"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
dataset = load_dataset("vidore/colpali_train_set", split="train")

# Group by source
source_splits = defaultdict(list)
for example in tqdm(dataset, desc="Categorizing"):
    source_splits[example['source']].append(example)

# Save each split as a Parquet file
for source, examples in source_splits.items():
    print(f"{source}: {len(examples)} examples")
    file_path = os.path.join(output_dir, f"{source}.parquet")

    # Convert to HuggingFace Dataset then save as Parquet
    hf_dataset = Dataset.from_list(examples)
    hf_dataset.to_parquet(file_path)

print(f"Saved {len(source_splits)} source-based splits as Parquet to {output_dir}/")
