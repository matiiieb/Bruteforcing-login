import random

def generate_address(country):
    if country == "United States":
        # List of possible states in the United States
        states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        # Generate a random address in the United States
        address = str(random.randint(100, 999)) + " " + random.choice(["Main St", "1st Ave", "2nd Ave", "Park Ave", "Broadway", "High St"]) + ", " + random.choice(states) + " " + str(random.randint(10000, 99999))
    elif country == "Canada":
        # List of possible provinces in Canada
        provinces = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan"]
        # Generate a random address in Canada
        address = str(random.randint(100, 999)) + " " + random.choice(["Main St", "1st Ave", "2nd Ave", "Park Ave", "Broadway", "High St"]) + ", " + random.choice(provinces) + " " + str(random.randint(1, 999999))
    else:
        # Default to a generic address if country is not recognized
        address = str(random.randint(100, 999)) + " " + random.choice(["Main St", "1st Ave", "2nd Ave", "Park Ave", "Broadway", "High St"]) + ", " + country
    return address

# Example usage
print(generate_address("United States"))
print(generate_address("Canada"))
print(generate_address("Australia"))
