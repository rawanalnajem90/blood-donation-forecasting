import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
try:
    df = pd.read_csv('transfusion.csv')
except FileNotFoundError:
    print("Error: Could not find 'transfusion.csv'. Make sure this script is running in the same folder as your dataset!")
    exit()

# Standardizing column names from the raw UCI Transfusion schema for clean visualizations
rename_dict = {
    'whether he/she donated blood in March 2007': 'Donated Again',
    'Made Donation in March 2007': 'Donated Again',
    'Target': 'Donated Again'
}
df.rename(columns=rename_dict, inplace=True)

# Double check dynamic naming variations for safety
for col in df.columns:
    if 'donated' in col.lower() or 'target' in col.lower() or 'return' in col.lower():
        df.rename(columns={col: 'Donated Again'}, inplace=True)

# Find the exact columns dynamically based on common keywords
recency_col = [c for c in df.columns if 'recency' in c.lower()][0]
frequency_col = [c for c in df.columns if 'frequency' in c.lower()][0]

# Set the visualization styling theme
sns.set_theme(style="whitegrid")

print("Generating portfolio visual files...")

# Chart 1: Target Distribution Chart
plt.figure(figsize=(6, 4))
ax1 = sns.countplot(x='Donated Again', data=df, palette='Set2')
plt.title('Distribution of Target Variable (Donated Again)')
plt.xlabel('Donation Status')
plt.ylabel('Count')
if sorted(df['Donated Again'].unique()) == [0, 1]:
    ax1.set_xticklabels(['No (0)', 'Yes (1)'])
plt.savefig('target_distribution.png', bbox_inches='tight')
plt.close()

# Chart 2: Recency Boxplot Chart
plt.figure(figsize=(6, 4))
ax2 = sns.boxplot(x='Donated Again', y=recency_col, data=df, palette='Set1')
plt.title('Recency vs Donation Status')
plt.xlabel('Donated Again')
plt.ylabel('Recency (Months Since Last Donation)')
if sorted(df['Donated Again'].unique()) == [0, 1]:
    ax2.set_xticklabels(['No (0)', 'Yes (1)'])
plt.savefig('recency_boxplot.png', bbox_inches='tight')
plt.close()

# Chart 3: Frequency vs Recency Scatter Chart
plt.figure(figsize=(7, 5))
sns.scatterplot(x=recency_col, y=frequency_col, hue='Donated Again', data=df, palette='coolwarm', alpha=0.8)
plt.title('Donation Frequency vs Recency')
plt.xlabel('Recency (months)')
plt.ylabel('Frequency (times)')
plt.savefig('frequency_vs_recency.png', bbox_inches='tight')
plt.close()

print("\nSuccess! The 3 portfolio images have been extracted and saved to your directory:")
print("1. target_distribution.png\n2. recency_boxplot.png\n3. frequency_vs_recency.png")