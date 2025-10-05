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
  import pandas as pd
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


#### Alternate function, selecting a specific threshold (higher than t active cases): ###
def analyze_covid_t(filename,t):
  '''
  Returns the cases of covid by country using a threshold (t). 
  Also returns the number of countries and 
  the average death/confirmed for countries with
  active cases higher than the threshold
  for covid cases using the filename specified as input.
  '''
  import pandas as pd
  df = pd.read_csv(filename)
  df['death_confirmed'] = df['Deaths'] / df['Confirmed']
  filtered_df = df[df['Active'] > t]
  print(f'\nMean of death_confirmed for countries with more than {t} active cases: {filtered_df["death_confirmed"].mean()}')
  print(f'\nNumber of countries with more than {t} active cases: {filtered_df['Country'].count()}\n')
  return filtered_df

t = 1000
print(analyze_covid_t(filename,t))

### EXTRA: Analyze cases by intervals ###
def analyze_covid_interval(filename):
  '''
  Returns the cases of covid by country using intervals. 
  Also returns a dataframe with number of countries and 
  the average death/confirmed by interval)
  for covid cases using the filename specified as input.
  '''
  import pandas as pd
  df = pd.read_csv(filename)
  bins = [0, 500,1000,5000, df['Active'].max() + 1] # Ensure the last bin edge is greater than the max age
  labels = ['<=500','>500', '>1000', '>5000']
  df['interval'] = pd.cut(df['Active'], bins=bins, labels=labels, right=False, duplicates='drop')
  
  df['death_confirmed'] = df['Deaths'] / df['Confirmed']
  df = df.sort_values('Active')
  average_death_confirmed_and_count = df.groupby('interval', observed=False).agg(
      average_death_confirmed=('death_confirmed', 'mean'),
      number_of_countries=('Country', 'count')
  ).reset_index()
  return average_death_confirmed_and_count

print('\n')
print(analyze_covid_interval(filename))