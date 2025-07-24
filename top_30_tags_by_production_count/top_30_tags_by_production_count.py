# !/usr/bin/env python3
"""
Plot top 30 tags by number of productions in anime
"""
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('top_30_tags_by_production_count/tag_production_counts.csv')

top_n = data.sort_values('NumberOfProductions', ascending=False).head(30)

# Plot
plt.figure(figsize=(12, 8))
plt.barh(top_n['Tag'], top_n['NumberOfProductions'])
plt.xlabel('Number of Productions')
plt.ylabel('Tags')
plt.title('Top 30 Tags by Number of Productions')
plt.gca().invert_yaxis()  # To display the highest value at the top
plt.show()