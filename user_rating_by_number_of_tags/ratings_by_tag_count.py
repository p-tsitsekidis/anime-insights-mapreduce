#!/usr/bin/env python3
"""
Plot user ratings by number of tags
"""
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('user_rating_by_number_of_tags/anime_tag_count_and_ratings.csv')

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['Number_of_Tags'], data['Rating'])
plt.title('User Ratings by Number of Tags')
plt.xlabel('Number of Tags')
plt.ylabel('User Rating')
plt.grid(True)
plt.show()