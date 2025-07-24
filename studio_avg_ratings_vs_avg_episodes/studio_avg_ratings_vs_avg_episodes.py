# !/usr/bin/env python3
"""
Plot average episodes by average ratings.
"""
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('studio_avg_ratings_vs_avg_episodes/studio_avg_episodes_and_ratings.csv')

# Bar Plot
plt.figure(figsize=(10, 6))
plt.bar(data['Avg_Episodes'], data['Avg_Rating'])
plt.title('Average Episodes by Average Rating')
plt.xlabel('Average Episodes')
plt.ylabel('Average Rating')
plt.show()