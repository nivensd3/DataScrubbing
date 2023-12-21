import GSearch


import pandas as pd

df = pd.read_excel('Data_Practice_Sheet.xlsx')

#Linkedin Reference for getting the Location 

#df = df.drop(['linkedinProfileUrl','Contact Name', 'Organization'], axis=1)

# Add a new column 'websites' and initialize it with an empty string
df['Websites'] = ''


#Index(['First_Name', 'Last_Name', 'Degree'], dtype='object')

for index in df.index:
    website = GSearch.search(df['First Name'][index], df['Last Name'][index], df['Business Email'][index])
    df.at[index, 'websites'] = website

df.to_excel('New_Data.xlsx', index=False,)