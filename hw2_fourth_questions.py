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

def analyze_covid(filename):
  '''
  Returns the countries that have more than 500, more than 1000 and 
  more than 5000 active cases in a list. 
  Also returns a dataframe with number of countries and 
  the average death/confirmedthe results by threshold 
  (more than 500, 1000 and 5000 active cases)
  for covid cases using the filename specified as input.
  '''
  df = pd.read_csv(filename)

  thresholds = [500, 1000, 5000]
  results = []

  for threshold in thresholds:
      filtered_df = df[df['Active'] > threshold]
      average_death_confirmed = (filtered_df['Deaths'] / filtered_df['Confirmed']).mean()
      countries = ', '.join(filtered_df['Country'].tolist())
      num_countries = len(filtered_df)
      results.append({
          'Threshold': threshold, 
          'Number of Countries': num_countries,
          'Average Death/Confirmed': average_death_confirmed, 
          'Countries': countries, 
          })

  results_df = pd.DataFrame(results)

  # Print the countries for each threshold inside the function
  def countries_thresh(value):
      res = results_df[results_df['Threshold'] == value]['Countries'].iloc[0]
      return res
  print(f'\nMore than 500 active cases: {countries_thresh(500)}')
  print(f'\nMore than 1000 active cases: {countries_thresh(1000)}')
  print(f'\nMore than 5000 active cases: {countries_thresh(5000)}\n')
  
  return results_df

# Analyze the covid_df DataFrame and display the results
print(analyze_covid(filename))