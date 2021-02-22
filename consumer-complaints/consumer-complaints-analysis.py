#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %% [code]
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import widgets

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %% [markdown]
# ### 1. Read Data

# %% [code]
# import pandas as pfd
df = pd.read_csv('/kaggle/input/consumer-complaint-database/complaints.csv')
df.head(5)

# %% [markdown]
# ### 2. Explore Data 

# %% [code]
df.isna().sum()

# %% [markdown]
# ### Q1. Which type product had the most complaints ordered by state?

# %% [code]
state_product_df = df.groupby(['State', 'Product']).size().sort_values(ascending=False)
print(state_product_df.head(10))

# %% [markdown]
# ### Q2. How many complaints have been filed for each company?

# %% [code]
complaints_by_company = df.groupby('Company').Company.count().sort_values(ascending=False)
print(len(complaints_by_company))
print(complaints_by_company)

# %% [markdown]
# ### Q3. Summarize the responses for each company.

# %% [markdown]
# #### Q3.1 All the responses visualized

# %% [code]
plt.figure(figsize = (15,6))
plt.xticks(rotation="50", ha="right", size = 10)
g = sns.countplot(x ="Company response to consumer", data = df, 
                  order = df['Company response to consumer'].value_counts().index)
g.set_xlabel("Response to Consumer complaint", fontsize=25)
g.set_ylabel("Count", fontsize=25)

# %% [markdown]
# #### Q3.2 Responses summarized for each company

# %% [code]
company_responses = df.groupby(['Company', 'Company response to consumer']).size()
print(company_responses.head(5))

