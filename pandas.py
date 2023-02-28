# PANDAS

# Pandas Series
# Reading Data
# Quick Look at Data
# Selection in Pandas
# Aggregation & Grouping
# Apply and Lambda
# Join Operations

# Pandas Series
import pandas as pd

# Creating a Pandas Series
s = pd.Series([10, 77, 12, 4, 5])

# Getting the type of the series
type(s)

# Getting the index of the series
s.index

# Getting the data type of the series
s.dtype

# Getting the size of the series
s.size

# Getting the number of dimensions of the series
s.ndim

# Getting the values of the series
s.values

# Getting the type of the values
type(s.values)

# Getting the first 3 values of the series
s.head(3)

# Getting the last 3 values of the series
s.tail(3)


# Reading Data
# Importing a csv file using Pandas
df = pd.read_csv("Python_Programming_for_Data_Science/Datasets/advertising.csv")

# Quick view of the data
df.head()


# Quick Look at Data
import seaborn as sns

# Loading the Titanic dataset using Seaborn
df = sns.load_dataset("titanic")

# Quick view of the first 5 rows of the data
df.head()

# Quick view of the last 5 rows of the data
df.tail()

# Getting the shape of the data
df.shape

# Getting information about the data
df.info()

# Getting the column names of the data
df.columns

# Getting the index of the data
df.index

# Getting a summary of the data
df.describe().T

# Checking if the data has any missing values
df.isnull().values.any()

# Getting the number of missing values in each column
df.isnull().sum()

# Getting the first 5 values of the "sex" column
df["sex"].head()

# Getting the count of each unique value in the "sex" column
df["sex"].value_counts()


# Selection in Pandas

# Loading the Titanic dataset using Seaborn
df = sns.load_dataset("titanic")

# Quick view of the first 5 rows of the data
df.head()

# Getting the index of the data
df.index

# Getting the first 13 rows of the data
df[0:13]

# Removing the first row of the data
df.drop(0, axis=0).head()

# Removing specific rows from the data
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# Making the "age" column as the index of the data
df.index = df["age"]

# Removing the "age" column
df.drop("age", axis=1).head()

# Removing the "age" column in place
df.drop("age", axis=1, inplace=True)
df.head()

# Convert Index to Variable

# Create a new column 'age' and set its value equal to the index
df["age"] = df.index

# Drop the 'age' column
df.drop("age", axis=1, inplace=True)

# Reset the index and show the first 5 rows
df = df.reset_index()


# Operations on Variables
df = sns.load_dataset("titanic")

# Check if 'age' is a column in the dataframe
"age" in df

# Show the first 5 values of the 'age' column
df["age"].head()

# Alternate method to access the 'age' column
df.age.head()

# Show the data type of the first 5 values of the 'age' column
type(df["age"].head())

# Show the first 5 rows of the 'age' column as a dataframe
df[["age"]].head()

# Show the data type of the first 5 rows of the 'age' column as a dataframe
type(df[["age"]].head())

# Show the first 5 rows of the 'age' and 'alive' columns
df[["age", "alive"]].head()

# Define a list of column names to select
col_names = ["age", "adult_male", "alive"]
df[col_names].head()

# Create new columns 'age2' and 'age3'
df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

# Drop the 'age3' column
df.drop("age3", axis=1).head()

# Drop the columns in the 'col_names' list
df.drop(col_names, axis=1).head()

# Drop all columns that contain the word 'age'
df.loc[:, ~df.columns.str.contains("age")].head()


# iloc & loc
df = sns.load_dataset("titanic")

# iloc: integer-based selection
# Show the first 3 rows of the dataframe
df.iloc[0:3]

# Show the first value of the first row
df.iloc[0, 0]

# loc: label-based selection
# Show the first 3 rows of the dataframe
df.loc[0:3]

# Show the first 3 rows of the first 3 columns
df.iloc[0:3, 0:3]

# Show the 'age' column for the first 3 rows
df.loc[0:3, "age"]

# Select specific columns
col_names = ["age", "embarked", "alive"]
df = df.loc[0:3, col_names]

# select rows where age is greater than 50
df = df[df["age"] > 50]

# count the number of rows where age is greater than 50
count = df["age"].count()

# select specific columns where age is greater than 50
df = df.loc[df["age"] > 50, ["age", "class"]]

# select specific columns where age is greater than 50 and sex is male
df = df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]]

# value counts of embark_town column
df["embark_town"].value_counts()

# select specific columns where age is greater than 50 and sex is male
# and embark_town is either Cherbourg or Southampton
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

# value counts of embark_town column in new dataframe
df_new["embark_town"].value_counts()

# Aggregation & Grouping

# group by sex and aggregate mean of age column
df.groupby("sex")["age"].mean()

# group by sex and aggregate mean of age column
df.groupby("sex").agg({"age": "mean"})

# group by sex and aggregate mean and sum of age column
df.groupby("sex").agg({"age": ["mean", "sum"]})

# group by sex, aggregate mean of age and mean of survived column
df.groupby("sex").agg({"age": ["mean", "sum"], "survived": "mean"})

# group by sex, embark_town and aggregate mean of age column
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"], "survived": "mean"})

# group by sex, embark_town, class and aggregate mean of age column
df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"], "survived": "mean"})

# group by sex, embark_town, class, aggregate mean of age, mean of survived and count of sex
df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"], "survived": "mean", "sex": "count"})

# Pivot table

# load the titanic dataset from seaborn library
df = sns.load_dataset("titanic")

# create pivot table with "survived" as values, "sex" as rows, and "embarked" as columns
df.pivot_table("survived", "sex", "embarked")

# create pivot table with "survived" as values, "sex" as rows, and multiple columns: "embarked" and "class"
df.pivot_table("survived", "sex", ["embarked", "class"])

# display the first 5 rows of the dataframe
df.head()

# create a new column with categorical values based on the age
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

# create pivot table with "survived" as values, "sex" as rows, and multiple columns: "new_age" and "class"
df.pivot_table("survived", "sex", ["new_age", "class"])

# set maximum width of display
pd.set_option('display.width', 500)


# Apply and Lambda

# Load Titanic dataset from seaborn
df = sns.load_dataset("titanic")

# Creating new columns with derived values from 'age' column
df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

# Displaying first 5 rows after dividing 'age' column by 10
(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

# Looping through all columns of the dataframe and printing the name of the column if it contains 'age'
for col in df.columns:
    if "age" in col:
        print(col)

# Looping through all columns of the dataframe and dividing the values by 10 if the column name contains 'age'
for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

# Looping through all columns of the dataframe and dividing the values by 10 and replacing the values in the original dataframe if the column name contains 'age'
for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

# Displaying first 5 rows of the dataframe after updating the values
df.head()

# Using apply function to divide the values by 10 for all columns that contain 'age'
df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

# Using apply function to divide the values by 10 and using string operations on column names to filter only columns that contain 'age'
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

# Using apply function to standardize the values for all columns that contain 'age'
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# Defining a function for standardization
def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

# Using the standart_scaler function to standardize the values for all columns that contain 'age'
df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# Replacing the standardized values in the original dataframe
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

# Displaying first 5 rows of the dataframe after replacing the standardized values
df.head()


# Joining Operations

# Create a numpy array with random values
m = np.random.randint(1, 30, size=(5, 3))

# Convert the numpy array to a pandas dataframe and specify the column names
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])

# Create a new dataframe by adding 99 to each element in df1
df2 = df1 + 99

# Concatenate the two dataframes vertically
pd.concat([df1, df2])

# Concatenate the two dataframes vertically and reset the index
pd.concat([df1, df2], ignore_index=True)


# Joining with Merge

# Create a dataframe containing employee names and group names
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

# Create a dataframe containing employee names and start dates
df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

# Merge the two dataframes on all columns that have matching names
pd.merge(df1, df2)

# Merge the two dataframes on the "employees" column
pd.merge(df1, df2, on="employees")

# Our goal is to access the information of each employee's manager
df3 = pd.merge(df1, df2)

# Create a dataframe containing group names and manager names
df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

# Merge the two dataframes on the "group" column
pd.merge(df3, df4)



