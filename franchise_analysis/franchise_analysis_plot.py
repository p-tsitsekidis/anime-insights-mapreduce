# !/usr/bin/env python3
"""
Generate bar charts visualizing franchise-level anime statistics.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("franchise_analysis/franchise_metadata.csv")  # Replace with your actual CSV file path

# Number of Anime per Franchise
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(df['_id'].head(30), df['numberOfAnime'].head(30), color='skyblue')
ax.set_title('Top 30 Franchises by Number of Anime')
ax.tick_params(axis='x', rotation=90)
ax.set_ylabel('Number of Anime')
plt.tight_layout()
plt.savefig("franchise_analysis/top_30_franchises_by_anime_count.png")
plt.close()

# Average Rating per Franchise
fig, ax = plt.subplots(figsize=(10, 7))
plt.bar(df['_id'].head(30), df['averageRating'].head(30), color='salmon')
plt.title('Top 30 Franchises by Average Rating')
plt.xticks(rotation=90)
plt.ylabel('Average Rating')
plt.tight_layout()
plt.savefig("franchise_analysis/top_30_franchises_by_average_rating.png")
plt.close()