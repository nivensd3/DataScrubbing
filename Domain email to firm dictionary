# List of financial companies and their domains
financial_companies = {
    'jpmorgan.com': 'JP Morgan',
    'goldmansachs.com': 'Goldman Sachs',
    'morganstanley.com': 'Morgan Stanley',
    'ameriprise.com': 'Ameriprise',
    'ml.com': 'Merrill Lynch',  # Merrill Lynch uses 'ml.com'
    'wellsfargo.com': 'Wells Fargo',
    'bankofamerica.com': 'Bank of America',
    'fidelity.com': 'Fidelity Investments',
    'ntrs.com': 'Northern Trust',  # Northern Trust uses 'ntrs.com'
    'citigroup.com': 'Citigroup Inc.',
    'blackrock.com': 'BlackRock, Inc.',
    'americanexpress.com': 'American Express',
    # Additional financial companies
    'barclays.com': 'Barclays',
    'hsbc.com': 'HSBC',
    'deutsche-bank.com': 'Deutsche Bank',
    'ubs.com': 'UBS',
    'credit-suisse.com': 'Credit Suisse',
    'bnymellon.com': 'BNY Mellon',
    # Add more companies and domains here
}

def detect_financial_company(email):
    # Extract domain from email
    domain = email.split('@')[-1]

    # Check if the domain is in the list of financial companies
    company = financial_companies.get(domain.lower())
    
    if company:
        return f"The email belongs to an employee of {company}."
    else:
        return "The company is not a recognized financial company or uses a generic email domain."

# Example Usage
email = "john.doe@ameriprise.com"
print(detect_financial_company(email))
