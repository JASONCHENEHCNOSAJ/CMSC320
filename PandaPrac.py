import pandas as pd
import numpy as np
"""(a) How do you select the rows of a Pandas DataFrame where a specific column is equal to
a certain value?
(b) How do you join two Pandas DataFrames on a specific column?
(c) How do you group a Pandas DataFrame by a specific column and calculate the mean of
another column?
(d) How do you convert a Pandas DataFrame to a NumPy array?
(e) How do you create a new column in a pandas dataframe that contains squared values of
another column?"""


# (a) How do you select the rows of a Pandas DataFrame where a specific column is equal to
# a certain value?
""" Ans: You do this by calling df.loc[]. The loc refers to a specific row in the
dataframe. So , if I do df.loc['row1'], I'm getting the contents of row1.
To get the rows where a specific columns meets a condition, you do
df.loc[df['col name'] == value]
"""

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
  
# print dataframe.
print(df)

# if i only want the rows where the Name column is nick,
print("if i only want the rows where the Name column is nick,", df.loc[df['Name'] == 'nick'])

# (b) How do you join two Pandas DataFrames on a specific column?
""" Ans: you join 2 pandas dataframes with the merge function
pd.merge()
You specify the columns with the "on" parameter
"""

# creating a dataframe
df1 = pd.DataFrame({'Name':['Raju', 'Rani', 'Geeta', 'Sita', 'Sohit'],
                    'Marks':[80, 90, 75, 88, 59]})
  
# creating another dataframe with different data
df2 = pd.DataFrame({'Name':['Raju', 'Divya', 'Geeta', 'Sita'],
                    'Grade':['A', 'A', 'B', 'A'],
                    'Rank':[3, 1, 4, 2 ],
                    'Gender':['Male', 'Female', 'Female', 'Female']})
  
# applying merge with more parameters
df1.merge(df2[['Grade', 'Name']], on = 'Name', how = 'left')

# (c) How do you group a Pandas DataFrame by a specific column and calculate the mean of
# another column?

# Ans: You use the groupby() and mean() function for dataframes
print(df.groupby('Name')['Age'].mean())