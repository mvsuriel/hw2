# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(x):
    return x * 3

# Examples
print(triple(3))  # should return 9
print(triple(10)) # should return 30
print(triple(-1)) # should return -3


# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(a, b):
    return a - b

# Examples
print(subtract(10, 4))  # should return 6
print(subtract(4, 10))  # should return -6


# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
# You should program the function and not use
# the function "dict" directly
def dictionary_maker(tuples):
    result = {}
    for key, value in tuples:
        result[key] = value
    return result

# Example
print(dictionary_maker([('foo', 1), ('bar', 3)]))

############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#
CV = [
    {'user': 'john', 'jobs': ['analyst', 'engineer']},
    {'user': 'jane', 'jobs': ['finance', 'software']},]


#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.
def has_experience_as(cvs, job_title):
    experienced_users = []
    for cv in cvs:
        if job_title in cv['jobs']:
            experienced_users.append(cv['user'])
    return experienced_users

# Examples
print(has_experience_as(CV, 'engineer'))  # should return ['john']
print(has_experience_as(CV, 'finance'))   # should return ['jane']
print(has_experience_as(CV, 'teacher'))   # should return []    


#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.
def job_counts(cvs):
    counts = {}
    for cv in cvs:
        for job in cv['jobs']:
            if job in counts:
                counts[job] += 1
            else:
                counts[job] = 1
    return counts

# Example
print(job_counts(CV))  # should return {'analyst': 1, 'engineeer': 1, 'finance': 1, 'software': 1}


#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.
def most_popular_job(cvs):
    counts = job_counts(cvs)
    most_popular = None
    highest_count = 0
    for job, count in counts.items():
        if count > highest_count:
            most_popular = job
            highest_count = count
    return (most_popular, highest_count)    

# Example
print(most_popular_job(CV))  # should return ('analyst', 1) or ('engineer', 1) or ('finance', 1) or ('software', 1) 


##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)


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


###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
#
# #
import pandas as pd
filename = 'https://raw.githubusercontent.com/mvsuriel/hw2/refs/heads/main/covid.csv'

def analyze_covid(df):
    """
    Filters countries by active cases and calculates the average death/confirmed ratio,
    returning the results in a DataFrame.
    Args:
        df (pd.DataFrame): DataFrame containing COVID-19 data.
    Returns:
        pd.DataFrame: A DataFrame with thresholds, countries, and average death/confirmed ratios.
    """
    df = pd.read_csv(filename)
    thresholds = [500, 1000, 5000]
    results = []

    for threshold in thresholds:
        filtered_df = df[df['Active'] > threshold]

        if not filtered_df.empty:
            average_death_confirmed = filtered_df['Deaths'].sum() / filtered_df['Confirmed'].sum()
            countries = ', '.join(filtered_df['Country'].tolist())
            results.append({'Threshold': threshold, 'Countries': countries, 'Average Death/Confirmed': average_death_confirmed})
        else:
            results.append({'Threshold': threshold, 'Countries': 'None', 'Average Death/Confirmed': 0}) # Or pd.NA

    return pd.DataFrame(results)

# Analyze the covid_df DataFrame and display the results
results_df = analyze_covid(filename)
print(results_df)

# Get the countries for each threshold
Threshold_500 = results_df[results_df['Threshold'] == 500]['Countries'].iloc[0]
Threshold_1000 = results_df[results_df['Threshold'] == 1000]['Countries'].iloc[0]
Threshold_5000 = results_df[results_df['Threshold'] == 5000]['Countries'].iloc[0]

# Print the countries for each threshold
print(f'Countries with more than 500 active cases: {Threshold_500}')
print(f'Countries with more than 1000 active cases: {Threshold_1000}')
print(f'Countries with more than 5000 active cases: {Threshold_5000}')