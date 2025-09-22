import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

# -------------------------------
# Load Data Function
# -------------------------------
@st.cache_data
def load_data(sample_size=None):
    usecols = ["title", "abstract", "publish_time", "authors", "journal", "source_x"]

    # Use sample CSV if full CSV not found
    csv_file = "metadata.csv"
    if not os.path.exists(csv_file):
        st.warning("metadata.csv not found. Using metadata_sample.csv instead.")
        csv_file = "metadata_sample.csv"

    try:
        if sample_size:
            df = pd.read_csv(csv_file, usecols=usecols).sample(n=sample_size, random_state=42)
        else:
            df = pd.read_csv(csv_file, usecols=usecols)
        return df
    except MemoryError:
        st.warning("MemoryError: falling back to a smaller sample (500 rows).")
        df = pd.read_csv(csv_file, usecols=usecols).sample(n=500, random_state=42)
        return df

# -------------------------------
# Load Dataset
# -------------------------------
df = load_data()

# Clean and prepare data
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Add abstract word count column
df["abstract_word_count"] = df["abstract"].dropna().apply(lambda x: len(str(x).split()))

# Drop rows missing essential info
df = df.dropna(subset=["title", "publish_time"])

# -------------------------------
# Streamlit App
# -------------------------------
st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers")

# Sidebar: Year filter
year_range = st.slider(
    "Select year range",
    int(df["year"].min()) if df["year"].notnull().any() else 2019,
    int(df["year"].max()) if df["year"].notnull().any() else 2022,
    (2020, 2021)
)

filtered = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# -------------------------------
# Visualizations
# -------------------------------

# 1️⃣ Publications by Year
st.subheader("Publications by Year")
year_counts = filtered["year"].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, palette="viridis", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
ax.set_title("Publications Over Time")
st.pyplot(fig)

# 2️⃣ Top 10 Journals
st.subheader("Top 10 Journals")
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, palette="magma", ax=ax)
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
ax.set_title("Top Journals Publishing COVID-19 Research")
st.pyplot(fig)

# 3️⃣ Word Cloud of Titles
st.subheader("Word Cloud of Paper Titles")
titles = " ".join(filtered["title"].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# 4️⃣ Distribution of Paper Counts by Source
st.subheader("Distribution of Paper Counts by Source")
source_counts = filtered["source_x"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=source_counts.values, y=source_counts.index, palette="coolwarm", ax=ax)
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Source")
ax.set_title("Top Sources of COVID-19 Papers")
st.pyplot(fig)

# 5️⃣ Abstract Word Count Distribution
st.subheader("Abstract Word Count Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered["abstract_word_count"].dropna(), bins=30, kde=True, color="skyblue", ax=ax)
ax.set_xlabel("Number of Words in Abstract")
ax.set_ylabel("Number of Papers")
ax.set_title("Distribution of Abstract Lengths")
st.pyplot(fig)

# -------------------------------
# Data Sample
# -------------------------------
st.subheader("Sample of Papers")
st.dataframe(filtered[["title", "journal", "year", "source_x", "abstract_word_count"]].head(20))
