# -*- coding: utf-8 -*-
"""DIC PROJECT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d4yzDawHVTNiBgFHCnppo-qFgDiYN611
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('/content/heart.csv')
df. index. size

df.head(10)

df.dtypes

df.describe()

"""**Renaming Columns**"""

df = df.rename(columns={'BMI': 'BodyMassIndex'})
df.head()

"""**Dealing Null Values**"""

df.isnull().sum()

df=df.dropna(axis='rows')
len(df. index)

df.isnull().sum()

"""**Removing Duplicates**"""

df.shape

df = df.drop_duplicates()
df.shape

"""**Dealing Datatypes**"""

df.dtypes

df['Race']=df['Race'].astype('string')
df['GenHealth']=df['GenHealth'].astype('string')

df.dtypes

"""**Dealing Numerical Values**"""

# df['Sex'].replace('Female',0,inplace=True)
# df['Sex'].replace('Male',1,inplace=True)
df['HeartDisease'].replace('Yes',1,inplace=True)
df['HeartDisease'].replace('No',0,inplace=True)
df['Smoking'].replace('Yes',1,inplace=True)
df['Smoking'].replace('No',0,inplace=True)
df['AlcoholDrinking'].replace('Yes',1,inplace=True)
df['AlcoholDrinking'].replace('No',0,inplace=True)
df['Stroke'].replace('Yes',1,inplace=True)
df['Stroke'].replace('No',0,inplace=True)
df['DiffWalking'].replace('Yes',1,inplace=True)
df['DiffWalking'].replace('No',0,inplace=True)
df['Diabetic'].replace('Yes',1,inplace=True)
df['Diabetic'].replace('No',0,inplace=True)
df['PhysicalActivity'].replace('Yes',1,inplace=True)
df['PhysicalActivity'].replace('No',0,inplace=True)
df['Asthma'].replace('Yes',1,inplace=True)
df['Asthma'].replace('No',0,inplace=True)
df['KidneyDisease'].replace('Yes',1,inplace=True)
df['KidneyDisease'].replace('No',0,inplace=True)
df['SkinCancer'].replace('Yes',1,inplace=True)
df['SkinCancer'].replace('No',0,inplace=True)

# df['Sex'].fillna(0, inplace=True)
# df['Sex'] = df['Sex'].astype(int)

df.head(10)

"""**Understanding the Data**"""

mean_value = df['HeartDisease'].mean()
median_value = df['HeartDisease'].median()
print("Mean:", mean_value)
print("Median:", median_value)
plt.figure(figsize=(4, 4))
sns.distplot(df['HeartDisease'], hist=False, rug=True)
plt.axvline(mean_value, color='r', linestyle='--', label='Mean')
plt.axvline(median_value, color='g', linestyle='-', label='Median')
plt.title('Distance Plot of Heart Disease')
plt.xlabel('Values')
plt.ylabel('Density')
plt.legend()
plt.show()

"""**Dealing Categorical Data**"""

encode_AgeCategory = {'55-59': 57, '80 or older': 80, '65-69': 67,
                      '75-79': 77, '40-44': 42, '70-74': 72, '60-64': 62,
                      '50-54': 52, '45-49': 47, '18-24': 21, '35-39': 37,
                      '30-34': 32, '25-29': 27}
df['AgeCategory'] = df['AgeCategory'].apply(lambda x: encode_AgeCategory.get(x, x))
df['AgeCategory'] = df['AgeCategory'].astype(int)
df = df.rename(columns={'AgeCategory': 'Age'})
df.head()

df.info()

"""**Dealing Unwanted Columns**"""

correlation_matrix = df.corr()
plt.figure(figsize=(8, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

df.drop(columns=['SleepTime'], inplace=True)

"""**Normalizing using MinMax Scalar**"""

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['BodyMassIndex_scaled'] = scaler.fit_transform(df[['BodyMassIndex']])
print(df[['BodyMassIndex', 'BodyMassIndex_scaled']])

"""**Dealing With Skewness**"""

skewness = df['BodyMassIndex'].skew()
plt.figure(figsize=(4, 4))
sns.distplot(df['BodyMassIndex'])
plt.show()

df['BodyMassIndex'] = np.log(df['BodyMassIndex'])
plt.figure(figsize=(4, 4))
sns.distplot(df['BodyMassIndex'])
plt.show()

df.drop(columns=['BodyMassIndex'], inplace=True)

"""**Expolatory Data Analytics**"""

fig, axes = plt.subplots(2, 1, figsize=(6,6))

sns.histplot(data=df, x='Age', bins=10, kde=False, color='skyblue', ax=axes[0])
axes[0].set_title('Age Distribution (Histogram)')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequency')

sns.kdeplot(data=df, x='Age', color='orange', shade=True, ax=axes[1])
axes[1].set_title('Age Distribution (KDE)')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Density')

plt.tight_layout()
plt.show()

import seaborn
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 6))
health = df['GenHealth'].value_counts()
axes[0].set_title("General Health Distribution", fontsize=12, weight='bold')
palette_color = seaborn.color_palette('pastel')
axes[0].pie(health, labels=health.index, radius=1, autopct='%.2f%%', colors=palette_color)
axes[0].axis('equal')
ethnicity = df['Race'].value_counts()
axes[1].set_title("Ethnicity", fontsize=12, weight='bold')
palette_color = seaborn.color_palette('pastel')
axes[1].pie(ethnicity, labels=ethnicity.index, radius=1, autopct='%.2f%%', colors=palette_color, textprops={'fontsize': 8})
axes[1].axis('equal')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
sns.countplot(x='GenHealth', hue='HeartDisease', data=df)
plt.title('General Health Vs Heart Disease')
plt.ylabel('Count')
plt.xlabel('General Health Condition')
plt.legend(title='Heart Disease')
plt.show()

correlation_matrix = df.corr()
plt.figure(figsize=(6, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

plt.figure(figsize=(12, 6))
ax =sns.countplot(x='Race', hue='HeartDisease', data=df)
plt.title('Race Vs Heart Disease')
plt.ylabel('Count')
plt.xlabel('Ethinicity & Heart Disease')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.legend(title='Heart Disease')
plt.show()

plt.figure(figsize=(10, 5))
x = sns.countplot(data=df, x='Sex', hue='HeartDisease')
plt.title("Prevalence of Heart Attacks Among Different Genders", fontsize=12)
plt.xlabel("Had Heart Attack", fontsize=10)
plt.ylabel("Individuals", fontsize=10)
for c in x.containers:
    x.bar_label(c)
plt.show()

plt.figure(figsize=(10, 5))
x = sns.countplot(data=df, x='Age', hue='HeartDisease')
plt.title("Prevalence of Heart Attacks Among Different Age Groups", fontsize=12)
plt.xlabel("Had Heart Attack", fontsize=10)
plt.ylabel("Individuals", fontsize=10)
for c in x.containers:
    x.bar_label(c)
plt.show()
df.head()

chronic_diseases = df[['HeartDisease','Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Diabetic', 'Asthma', 'KidneyDisease', 'SkinCancer']]
plt.figure(figsize=(18,15))
for i,column in enumerate(chronic_diseases.columns[1:],1):
    plt.subplot(3,3,i)
    ax = sns.countplot(data=chronic_diseases, x=column, hue='HeartDisease')
    ax.set_title('Correlation b/w Heart Attack and '+column[:], fontsize = 12, weight='bold')
    ax.set_xlabel(column, fontsize = 10, weight='bold')
    ax.set_ylabel('People count', fontsize = 10, weight='bold')
    for container in ax.containers:
        ax.bar_label(container)
plt.suptitle('Different diseases and habits comparison with heart attack', size=25, fontweight='bold')
plt.tight_layout(w_pad=1, h_pad=2)

sns.pairplot(df,height=1)
plt.show()

df.hist(figsize=(6,6), bins=40, xlabelsize=6, ylabelsize=6);

plt.figure(figsize=(6,6))
sns.scatterplot(data=df, x='BodyMassIndex_scaled', y='Age', hue='HeartDisease')
plt.title('Scatter Plot of BMI vs Age by Heart Disease Status')
plt.xlabel('BMI')
plt.ylabel('Age')
plt.legend(title='Heart Disease')
plt.show()