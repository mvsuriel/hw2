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
import pandas as pd

filename = 'https://raw.githubusercontent.com/mvsuriel/hw2/refs/heads/main/covid.csv'

def analyze_covid(df):
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