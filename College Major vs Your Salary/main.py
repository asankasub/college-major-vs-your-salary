import pandas as pd

df = pd.read_csv('C:/Users/Asanka/Desktop/Python Practice/College Major vs Your Salary/salaries_by_college_major (1).csv')

# To view the first 5 rows of the data frame:
print(df.head())
# To find the number of rows and columns:
print(df.shape)
#To find the name of each column:
print(df.columns)
#To find if there are any NaN values:
print(df.isna())
#To view the last five rows on the data frame:
print(df.tail())
#To remove Nan values:
clean_df = df.dropna()
#To access the Starting Median Salary column in the data frame:
print(clean_df['Starting Median Salary'])
#To find the highest starting median salary:
print(clean_df['Starting Median Salary'].max())
#To find the index of the row with the largest value:
print(clean_df['Starting Median Salary'].idxmax())
#To see the name of the major that corresponds to that particular row:
print(clean_df['Undergraduate Major'].loc[43])
#Or you can do:
print(clean_df['Undergraduate Major'][43])
#If you don't specify a particular column you can use the .loc property to retrieve an entire row:
print(clean_df.loc[43])
#What college major has the highest mid-career salary? How much do graduates with this major earn?
major_max_mid= clean_df['Undergraduate Major'][clean_df['Mid-Career Median Salary'].idxmax()]
major_max_mid_salary = clean_df['Mid-Career Median Salary'].max()
print(major_max_mid_salary)
print(major_max_mid)
#Which college major has the lowest starting salary and how much do graduates earn after university?
major_min_start = clean_df['Undergraduate Major'][clean_df['Starting Median Salary'].idxmin()]
major_min_start_salary = clean_df['Starting Median Salary'].min()
print(major_min_start)
print(major_min_start_salary)
#Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
major_min_mid = clean_df['Undergraduate Major'][clean_df['Mid-Career Median Salary'].idxmin()]
major_min_mid_salary = clean_df['Mid-Career Median Salary'].min()
print(major_min_mid)
print(major_min_mid_salary)
#To find the difference between two columns:
spread = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
print(spread)
#Alternatively:
subtract_spread = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])
print(subtract_spread)
#To include a data frame in an existing one:
clean_df.insert(1,'Spread',spread)
clean_df.head()
print(clean_df.head())
#To find the degrees with the smallest spread:
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())
#What are the top 5 degrees with the highest values in the 90th percentile?
top_five_degrees = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(top_five_degrees[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
#What are the top 5 degrees with the greatest spread in salaries? 
biggest_spread = clean_df.sort_values('Spread', ascending=False)
print(biggest_spread[['Undergraduate Major','Spread']].head())
#To count majors by category:
print(clean_df.groupby('Group').count())
#To find the average salary by group:
print(clean_df.groupby('Group').mean())
#To round this:
pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').mean())



