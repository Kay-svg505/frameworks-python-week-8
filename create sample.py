import pandas as pd

# Columns we need
usecols = ["title", "abstract", "publish_time", "authors", "journal", "source_x"]

# Load the full metadata (adjust path if needed)
df = pd.read_csv("metadata.csv", usecols=usecols)

# Take a random sample of 500 rows
sample_df = df.sample(n=500, random_state=42)

# Save as a new CSV
sample_df.to_csv("metadata_sample.csv", index=False)

print("Sample CSV created: metadata_sample.csv")
