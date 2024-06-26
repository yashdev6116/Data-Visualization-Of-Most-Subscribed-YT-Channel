# -*- coding: utf-8 -*-
"""Data Visualization Of Most Subscribed YouTube Channels.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lnplbePgQhc9aIMOWBAXuwqeOJWxze1y
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
upload=files.upload()

data = pd.read_csv('/content/Most Subscribed YouTube Channels_exported.csv')

data.head()

data.tail()

print(data.describe())

data.info()
data.describe()



view=data.groupby(['Category','Brand channel'])['Subscribers (millions)'].sum().reset_index()
view

data.groupby(['Country'])['Subscribers (millions)'].sum()



# Histograms for each numerical column
data.hist(figsize=(10, 10))
plt.show()

# Pairplot for pairwise relationships in the dataset
sns.pairplot(data)
plt.show()

# Boxplot for visualizing the distribution of numerical variables
plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.xticks(rotation=45)  # Rotating x-axis labels for better readability
plt.show()

print("Column Names:", data.columns.tolist())

category_counts = data['Country'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Categories')
plt.axis('equal')
plt.show()

category_counts = data['Brand channel'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Categories')
plt.axis('equal')
plt.show()

# taking column "Primary language"
category_counts = data['Primary language'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Categories')
plt.axis('equal')
plt.show()

#taking column "Category"
category_counts = data['Category'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Categories')
plt.axis('equal')
plt.show()

# Group data by country and sum the subscribers
country_counts = data.groupby('Country')['Subscribers (millions)'].sum().sort_values(ascending=False)
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x=country_counts.index, y=country_counts.values, palette="viridis")
plt.xlabel('Country', fontsize=12)
plt.ylabel('Total Subscribers (Millions)', fontsize=12)
plt.title('Subscribers by Country (Millions)', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

