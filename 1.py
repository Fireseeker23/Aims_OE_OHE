import pandas as pd
import numpy as np

#data
test_data = 'data/test.csv'
home_data = pd.read_csv(test_data)


#Imputer

col_missing = []
for col in home_data.columns:
    if home_data[col].isnull().any():
        col_missing.append(col)

for col in col_missing:
    home_data[col] = home_data[col].fillna(0)

#cat columns

cat_columns = []
for col in home_data.columns:
    if home_data[col].dtype == 'object':
        cat_columns.append(col)

#Ordinal encoder
def OE(cat_columns, home_data):
    i = 0
    for col in cat_columns:
        unique_elements = home_data[cat_columns[i]].unique()
        j = 0 
        while j < len(unique_elements):
            k = 0
            while k < len(home_data[cat_columns[i]]):
                if home_data.loc[k,cat_columns[i]] == unique_elements[j]:
                    home_data.loc[k,cat_columns[i]] = j + 1
                k = k + 1
            j = j + 1
        i = i + 1



#One hot encoder
def OHE(cat_columns, home_data):
    new_columns = {}
    for col in cat_columns:
        unique_elements = home_data[col].unique()
        for unique_value in unique_elements:
            new_columns[f"{col}_{unique_value}"] = (home_data[col] == unique_value).astype(int)

    new_columns = pd.DataFrame(new_columns)
    home_data.drop(cat_columns, axis=1, inplace=True)
    home_data = pd.concat([home_data, new_columns], axis=1)


print(home_data)
print(len(cat_columns))
Type = input("Enter 0 for Ordinal Encoding and 1 for One Hot Encoding: ")
if Type == '0':
    OE(cat_columns, home_data)
    print(home_data.head())
elif Type == '1':
    OHE(cat_columns, home_data)
    print(home_data.tail())






