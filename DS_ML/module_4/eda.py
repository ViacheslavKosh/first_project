import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Завантаження датасету

df = sns.load_dataset('iris')

# Перегляд перших рядків даних

print(df.head())

# Основні статистичні характеристики

print(df.describe())

# Перевірка на пропущені значення

print(df.isnull().sum())

# Візуалізація розподілу змінної

sns.histplot(df['sepal_length'], kde=True)
plt.show()

# Візуалізація взаємозв'язку між змінними

sns.pairplot(df, hue='species')
plt.show()
