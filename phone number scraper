import re

def extract_phone_number(text):
    # Regular expression pattern for a phone number
    # This pattern is for a phone number format like 123.456.7890
    pattern = r'\d{3}\.\d{3}\.\d{4}'

    # Search for the pattern in the text
    match = re.search(pattern, text)

    # If a match is found, return it
    if match:
        return match.group()
    else:
        return "No phone number found."

# Example usage
text = """... your provided text ..."""
phone_number = extract_phone_number(text)
print(phone_number)
