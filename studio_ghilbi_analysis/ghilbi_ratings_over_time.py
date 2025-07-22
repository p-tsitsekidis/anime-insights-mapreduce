#!/usr/bin/env python3
"""
Plot Studio Ghibli anime ratings by release year.
"""
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = pd.read_csv('studio_ghilbi_analysis/task1.csv')

# Bar Plot
plt.figure(figsize=(10, 6))
plt.bar(data['Release_year'], data['Rating'])
plt.title('Studio Ghibli Anime Ratings by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Rating')
plt.show()