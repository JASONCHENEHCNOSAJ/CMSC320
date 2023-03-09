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
# This finds groups the dataframe by name and calculates the mean of the Age column

print(df.groupby('Name')['Age'].mean())

# (d) How do you convert a Pandas DataFrame to a NumPy array?
# Ans:You use the pandas dataframe to_numpy() function
# this takes a dataframe and converts it to a numpy 2darray with with each element representing a column in df
fields = {
    
    'Champion': ['Irelia','Sona','Garen'],
    'Type': ['Melee','Range','Melee'],
    'Lane': ['Top','Support','Top'],
    'Age': [23,20,19]
    
}
df = pd.DataFrame(fields)
print("LOL Dataframe", df)

#Turning it to numpy arr using to_numpy()

print("LOL df as a numpy arr", df.to_numpy())

# (e) How do you create a new column in a pandas dataframe that contains squared values of
# another column?

# Ans: You do this using the .apply() function. you call your df and initialize the name of your new column. Then you
# reference the column you want to base your new values off of followed by the apply function and referencing labmda x:
# sort of like a for loop for each value of age
df['sq Age'] = df['Age'].apply(lambda x: x*x)

print("dataframe after adding new columns is", df)
