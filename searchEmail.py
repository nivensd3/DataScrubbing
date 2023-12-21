import pandas as pd
import GSearch

def search_business_email(first_name, last_name):
    # Construct a query using the provided names
    query = f"{first_name} {last_name} business email"

    service = build('customsearch', 'v1', developerKey=API_KEY)

    try:
        # Perform a search using the Custom Search JSON API
        result = service.cse().list(q=query, cx=CX).execute()

        # Check if results are found
        if 'items' in result:
            # Extract and return the business email (or any relevant information)
            return result['items'][0].get('pagemap', {}).get('person', [{}])[0].get('email', None)
        else:
            print(f"No results found for {first_name} {last_name}.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    df = pd.read_excel('Data_Practice_Sheet.xlsx')

    # Add a new column 'business_email' and initialize it with an empty string
    df['business_email'] = ''

    # Loop through the DataFrame and call the modified search function
    for index in df.index:
        first_name = df['First Name'][index]
        last_name = df['Last Name'][index]

        # Check if either first name or last name is not present
        if pd.isnull(first_name) or pd.isnull(last_name):
            business_email = search_business_email(first_name, last_name)
            df.at[index, 'business_email'] = business_email

    # Export the DataFrame to a new Excel file
    df.to_excel('New_Data_with_Emails.xlsx', index=False)
