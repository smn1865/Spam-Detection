import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string


df = pd.read_csv("spam.csv",encoding='latin-1')
print(df['Class'].value_counts(normalize=True))

df['Length'] = df['Message'].str.len()

df['Message'] = df['Message'].str.translate(str.maketrans('','',string.punctuation))

df = df['Message'].str.lower().str.split()
print(df.head())

