import pandas as pd

df = pd.read_excel('Data_Practice_Sheet.xlsx')

for index in df.index:
    first_name = str(df['First Name'][index])  # Convert to string
    last_name = str(df['Last Name'][index])  # Convert to string

    # Concatenate the strings and assign to 'Contact Name'
    df.loc[index, 'Contact Name'] = first_name + ' ' + last_name

df.to_excel('New_Data.xlsx', index=False)











'''
for index in df.index:
    df.loc[index, 'Contact Name'] = df['First Name'][index] + ' ' + df['Last Name'][index]

df.to_excel('New_Data.xlsx', index=False)
'''