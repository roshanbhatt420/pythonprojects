import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('earthquake_data_nepal.csv')
print(df.head())

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
# Assign variables
magnitude = df['Magnitude']
deaths = df['Deaths']
region = df['Region']
depth = df['Depth']
date = df['Year']

# Convert to numpy arrays
magnitude = np.array(magnitude)
deaths = np.array(deaths)
region = np.array(region)
depth = np.array(depth)
date = np.array(date)

# Bar graph of date vs deaths
plt.bar(date, deaths, color='orange', width=0.5, align='center', label='deaths', edgecolor='black')
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.title('Date vs Deaths')
plt.show()

# Time series graph of date vs magnitude
plt.plot(date, magnitude, color='blue', marker='o', linestyle='--', linewidth=2)
plt.xlabel('Date')
plt.ylabel('Magnitude')
plt.title('Date vs Magnitude')
plt.show()

# Scatter plot of magnitude vs deaths
plt.scatter(magnitude, deaths, color='red', marker='*')
plt.xlabel('Magnitude')
plt.ylabel('Deaths')
plt.title('Magnitude vs Deaths')
plt.show()

# Histogram of magnitude
plt.hist(magnitude, bins=10, color='green')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.title('Histogram of Magnitude')
plt.show()
