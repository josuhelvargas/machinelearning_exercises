import pandas as pd
import numpy as np
from sklearn.preprocessing import scale as scaleskl
import matplotlib.pyplot as plt
import seaborn as sns



def showData():
    creditcardDataset = pd.read_csv('~/Documents/datasets/Credit-card-dataset/creditcard.csv')
    print(creditcardDataset.head())
    print(creditcardDataset.describe())
    print(creditcardDataset.info())
    print(creditcardDataset.shape)
    print(creditcardDataset.columns)
    print(creditcardDataset.dtypes)


def scale(y, c=True, sc=True):
    x = y.copy()
    if c:
        x -= x.mean()
    if sc and c:
        x /= x.std()
    elif sc:
        x /= np.sqrt(x.pow(2).sum().div(x.count() - 1))
    return x


def preprocess():
    creditcardDataset = pd.read_csv('~/Documents/datasets/Credit-card-dataset/creditcard.csv')
    scaled = scale(creditcardDataset["Amount"])
    print(scaled)
    #scaled = scaled.drop(columns=['Time'], axis=1)
    #print(scaled.head())




preprocess()
