import requests
import pandas as pd

df = pd.read_excel('Data_Practice_Sheet.xlsx')



# BrokerCheck API endpoint and credentials
api_endpoint = 'https://api.finra.org/brokercheck'
api_key = 'YOUR_API_KEY'

# Example broker ID or name
broker_id = '123456'

headers = {
    'apikey': api_key,
    'Content-Type': 'application/json'
}

params = {
    'broker_id': broker_id
}

response = requests.get(api_endpoint, headers=headers, params=params)

if response.status_code == 200:
    broker_data = response.json()

    # Extract city and state information from broker_data
    city = broker_data['city']
    state = broker_data['state']  

    df['City'] = city
    df['State'] = state

    # Save the updated DataFrame to a new Excel file
    df.to_excel('New_Data.xlsx', index=False)

else:
    print("Failed to fetch data:", response.status_code)
