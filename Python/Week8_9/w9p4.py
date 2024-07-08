# Develop a python program read a dataset and perform the following using Pandas
# a. Display the data excluding the rows with empty or NA values. 
# b. Replace the NA values using mean of the column. 
# c. Replace the NA values using median of the column. 
# d. Display if the dataset has any duplicate entries or not.

import pandas as pd

iris = pd.read_csv("iris.csv")

iris.dropna()

iris.fillna(iris.mean())

iris.fillna(iris.median())

iris.duplicated()