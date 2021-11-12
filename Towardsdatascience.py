#Step 1 : importing the required libraries
import pandas as pd
import numpy as np
import csv
# Step 2: Getting the data-set from different source and displaying it.
url = 'https://raw.githubusercontent.com/WilliamJiemesha/HeartDiseaseCsv/main/heart.csv'
df1 = pd.read_csv(url)
print(df1.head(3))
# Step 3 : Removing the unused and irrelevant columns
df1 = df1.drop(['cp','fbs','restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'thal', 'target','ca'], axis= 1)
print(df1.head(5))
# Step 4: Renaming the column name as per our convienance
df1= df1.rename(columns= {"age": "Age", "sex": "Sex", "trestbps": "Bps", "chol": "Cholesterol"})
print (df1.head(5))
# Step 5: Replacing the values of the rows if necessary
replace_values = {0: "F", 1: "M"}
df1= df1.replace({"Sex":replace_values})
print (df1.head(5))
print (df1.tail(5))
