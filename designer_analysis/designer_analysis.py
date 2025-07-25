# !/usr/bin/env python3
"""
Analyze anime character designers based on total productions, number of studios collaborated with,
and highest average rating. Generates three bar charts showing the top 30 designers by each metric.
"""
import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_json("designer_analysis/designer_metadata.json")

# Getting the info from the nested studio
df['Num_Studios'] = df['studios'].apply(len)
df['Highest_Rating'] = df.apply(lambda x: max([studio['avgRating'] for studio in x['studios'] if studio.get('avgRating') is not None], default=None), axis=1)


# top 30
df_most_productions = df.nlargest(30, 'totalProductions')
df_most_studios = df.nlargest(30, 'Num_Studios')
df_highest_ratings = df.nlargest(30, 'Highest_Rating')

# Designers with the most productions
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(df_most_productions['designer'], df_most_productions['totalProductions'], color='skyblue')
ax.set_title('Top 30 Designers by Number of Productions')
ax.set_ylabel('Total Productions')
ax.set_xticklabels(df_most_productions['designer'], rotation=90)
plt.tight_layout()
plt.savefig("designer_analysis/top_30_designers_by_total_productions.png")
plt.close()

# Designers that have worked with the most unique studios
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(df_most_studios['designer'], df_most_studios['Num_Studios'], color='lightgreen')
ax.set_title('Top 30 Designers by Number of Studios Worked With')
ax.set_ylabel('Number of Studios')
ax.set_xticklabels(df_most_studios['designer'], rotation=90)
plt.tight_layout()
plt.savefig("designer_analysis/top_30_designers_by_studio_collaboration.png")
plt.close()

# Designers with the highest ratings
fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(df_highest_ratings['designer'], df_highest_ratings['Highest_Rating'], color='salmon')
ax.set_title('Top 30 Designers by Highest Rating')
ax.set_ylabel('Highest Average Rating')
ax.set_xticklabels(df_highest_ratings['designer'], rotation=90)
plt.tight_layout()
plt.savefig("designer_analysis/top_30_designers_by_highest_rating.png")
plt.close()