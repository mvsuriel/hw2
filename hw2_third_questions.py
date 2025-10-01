# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country
def total_registered_cases(data, country):
    if country in data:
        return sum(data[country])
    else:
        return 0

# Examples
data = {
    'Spain': [4, 8, 2, 0, 1], 
    'France': [2, 3, 6],
    'Italy': [6, 8, 1, 7]}
print(total_registered_cases(data, 'Spain'))   # should return 15
print(total_registered_cases(data, 'France'))  # should return 11
print(total_registered_cases(data, 'Italy'))   # should return 22
print(total_registered_cases(data, 'Germany')) # should return 0 

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#
def total_registered_cases_per_country(data):
    totals = {}
    for country, cases in data.items():
        totals[country] = sum(cases)
    return totals  

# Example
print(total_registered_cases_per_country(data))  # should return {'Spain': 15, 'France': 11, 'Italy': 22}

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases
def country_with_most_cases(data):
    totals = total_registered_cases_per_country(data)
    most_cases_country = None
    highest_cases = 0
    for country, cases in totals.items():
        if cases > highest_cases:
            most_cases_country = country
            highest_cases = cases
    return most_cases_country

# Example  
print(country_with_most_cases(data))  # should return 'Italy'   


# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases
def country_with_most_cases(data):
    totals = total_registered_cases_per_country(data)
    most_cases_country = None
    highest_cases = 0
    for country, cases in totals.items():
        if cases > highest_cases:
            most_cases_country = country
            highest_cases = cases
    return most_cases_country

# Example  
print(country_with_most_cases(data))  # should return 'Italy'   