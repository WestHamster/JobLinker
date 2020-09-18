import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import os

datapath = 'data'

path = os.getcwd()
files = os.listdir(datapath)

files_xls = [f for f in files if f[-3:]=='csv']

def operations_data(data):
    country = data['']

def reading_files(data_file):
    data1 = pd.read_csv('data/'+data_file,encoding = "ISO-8859-1")
    print(data1.head())
    print()
    print()
    print(data1.isnull().sum())
    print()
    print()
    print(data1.shape)
    print()

    return data1;

reading_files(files_xls[0])
