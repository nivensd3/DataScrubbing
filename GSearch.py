from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' and 'YOUR_CX' with your actual API key and Custom Search Engine ID
API_KEY = 'AIzaSyDYdUgu4pUBwFXiWsSfSA677byl1s2FVt0'
CX = '6077425abb7564e08'

def search(first_name, last_name, bus_email):
     
    query = f"{first_name} {last_name} {bus_email} website"

    service = build('customsearch', 'v1', developerKey=API_KEY)

    try:
        # Perform a search using the Custom Search JSON API
        result = service.cse().list(q=query, cx=CX).execute()

        # Print the first result
        if 'items' in result:
            for item in result['items']:
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print("\n")
        else:
            print("No results found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'cats' with the desired search query
    search('')
   
