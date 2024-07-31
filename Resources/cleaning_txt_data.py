# dependencies
import pandas as pd
import re

## Cleaning cleveland data into proper rows
path = r"./unclean_cleveland.txt"

with open(path, 'rb') as f:
  contents = f.read()
  
# Convert into string
data = contents.decode('utf-8', errors='ignore')

# Split the data by the keyword 'name'
rows = re.split(r'\s*name\s*', data)

# Remove any leading or trailing whitespace and empty strings
rows = [row.strip() for row in rows if row.strip()]

# Create cleveland full dataframe
c_df = pd.DataFrame(rows, columns = ['data'])
c_df

c_df = c_df['data'].str.split(expand=True).reindex(columns=range(75))
c_df

## Cleaning long beach va data into proper rows
path = r"./unclean_long_beach_va.txt"

with open(path, 'rb') as f:
  contents = f.read()
  
# Convert into string
data = contents.decode('utf-8', errors='ignore')

# Split the data by the keyword 'name'
rows = re.split(r'\s*name\s*', data)

# Remove any leading or trailing whitespace and empty strings
rows = [row.strip() for row in rows if row.strip()]

# Create long beach va full dataframe
v_df = pd.DataFrame(rows, columns = ['data'])
v_df

v_df = v_df['data'].str.split(expand=True)
v_df

# Add column names for both dataframes
col_names =  ['id', 'ccf', 'age', 'sex', 'painloc', 'painexer',
              'relrest', 'pncaden', 'cp', 'trestbps', 'htn',
              'chol', 'smoke', 'cigs (cigarettes per day)', 'years as smoker', 
              'fbs', 'diab', 'famhist', 'restecg', 'ekgmo', 'ekgday',
              'ekgyr', 'dig', 'prop', 'nitr', 'pro', 'diuretic', 
              'proto', 'thaldur', 'thaltime', 'met', 'thalach', 'thalrest', 
              'tpeakbps', 'tpeakbpd', 'dummy', 'trestbpd', 'exang', 'xhypo', 
              'oldpeak', 'slope', 'rldv5', 'rldv5e', 'ca', 'restckm', 'exerckm', 
              'restef', 'restwm', 'exeref', 'exerwm', 'thal', 'thalsev', 
              'thalpul', 'earlobe', 'cmo', 'cday', 'cyr', 'num', 'lmt', 'ladprox',
              'laddist', 'diag', 'cxmain', 'ramus', 'om1', 'om2', 'rcaprox', 
              'rcadist', 'lvx1', 'lvx2', 'lvx3', 'lvx4', 'lvf', 'cathef', 'junk']

c_df.columns = col_names
v_df.columns = col_names

# Display full dataframes
c_df.head()
v_df.head()

# Combine full dataframes as one
full_df = pd.concat([c_df, v_df], axis=0)
full_df

# Value counts for all columns
for col in full_df.columns:
    print("\n-----%s-----" % col)
    print(full_df[col].value_counts())

# Dataset Count
full_df.size  # 37050
full_df.shape  # 494,75

# Save full_df as csv file
full_df.to_csv("./full_dataset.csv", index=False)
