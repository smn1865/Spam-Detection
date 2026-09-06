import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string


df = pd.read_csv("spam.csv",encoding='latin-1')
print(df['Class'].value_counts(normalize=True))

df['Length'] = df['Message'].str.len()


df = pd.read_csv('spam.csv', encoding = 'latin-1')
print(df.describe())
print(df.head())
