import pandas as pd
import os

def extract_jobs(csv_path, output_dir):
    """
    Extracts the context column from the CSV file and saves each item as a text file.
    """
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(csv_path)
    context_data = df['context']

    for i, item in enumerate(context_data):
        with open(os.path.join(output_dir, f"job_{i}.txt"), 'w') as f:
            f.write(item)
