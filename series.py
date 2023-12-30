import requests

def get_serial_tests(first_name, last_name, api_key):
    # Replace with the actual endpoint for retrieving serial tests
    url = 'https://api.finra.org/serial_tests'

    # Headers for authentication (if required)
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    # Parameters for the request
    # Replace these with the actual parameter names as per the API documentation
    params = {
        'firstName': first_name,
        'lastName': last_name
    }

    # Make the request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and return the data
        return response.json()
    else:
        # Handle errors (you can expand on this with specific error messages)
        return f'Error: {response.status_code}'

# Example usage
api_key = 'YOUR_API_KEY'
first_name = 'John'
last_name = 'Doe'

# Call the function
test_results = get_serial_tests(first_name, last_name, api_key)
print(test_results)
