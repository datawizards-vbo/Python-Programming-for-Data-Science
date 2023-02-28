# Advanced Functional EDA

# Importing necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setting options to display all columns and wider width
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# Loading the Titanic dataset from seaborn
df = sns.load_dataset("titanic")


# 1. General Picture

# Quick look at the head and tail of the data
df.head()
df.tail()

# Getting the shape and information of the data
df.shape
df.info()

# Getting the columns and index of the data
df.columns
df.index

# Getting summary statistics of the data
df.describe().T

# Checking for missing values in the data
df.isnull().values.any()
df.isnull().sum()

# Function to get a detailed look at the data
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())


# 2. Analysis of Categorical Variables

# Load the Titanic dataset
df = sns.load_dataset("titanic")

# Display the first 5 rows of the dataframe
df.head()

# Display the count of the 'survived' column
df["survived"].value_counts()

# Display the unique values of the 'sex' column
df["sex"].unique()

# Display the number of unique values in the 'class' column
df["class"].nunique()

# Create a list of categorical columns, either of type 'category', 'object', or 'bool'
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# Create a list of numerical columns with less than 10 unique values
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

# Create a list of categorical columns with more than 20 unique values
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

# Add the numerical columns with less than 10 unique values to the list of categorical columns
cat_cols = cat_cols + num_but_cat

# Remove the categorical columns with more than 20 unique values from the list of categorical columns
cat_cols = [col for col in cat_cols if col not in cat_but_car]

# Display the number of unique values in each categorical column
df[cat_cols].nunique()

# Display the list of columns that are not categorical
[col for col in df.columns if col not in cat_cols]

# Display the ratio of the count of the 'survived' column
100 * df["survived"].value_counts() / len(df)

# Define a function to display the count and ratio of each category in a given column
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

# Use the 'cat_summary' function to display the count and ratio of each category in the 'sex' column
cat_summary(df, "sex")

# Use the 'cat_summary' function to display the count and ratio of each category in all categorical columns
for col in cat_cols:
    cat_summary(df, col)


def cat_summary(dataframe, col_name, plot=False):
    """
    This function takes in a pandas dataframe, a column name, and a boolean value (default=False) indicating
    whether or not to plot the data. It prints a summary of the value counts and ratios of the column,
    and if plot is True, it displays a countplot of the column.
    """
    # Create a dataframe containing the value counts and ratios of the specified column
    summary_df = pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                               "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)})

    # Print the summary dataframe
    print(summary_df)
    print("##########################################")

    # If plot is True, display a countplot of the column
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

# Example usage of the function
cat_summary(df, "sex", plot=True)

# Loop through the list of categorical columns
for col in cat_cols:
    # If the column is of type boolean, convert it to int
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)

# Example usage of the function with a boolean column
cat_summary(df, "adult_male", plot=True)

# Example usage of the function without plotting
cat_summary(df, "sex")


# 3. Analysis of Numerical Variables
# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set display options for pandas dataframe
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# Load titanic dataset
df = sns.load_dataset("titanic")

# Select categorical columns from the dataframe
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# Select numerical columns with less than 10 unique values as categorical columns
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

# Select categorical columns with more than 20 unique values as non-categorical columns
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

# Merge selected categorical columns and numerical columns as categorical columns
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

# Show descriptive statistics for age and fare columns of the dataframe
print(df[["age", "fare"]].describe().T)

# Select all numerical columns in the dataframe
num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

# Select numerical columns that are not categorical columns
num_cols = [col for col in num_cols if col not in cat_cols]

# Define a function to show summary statistics for a numerical column
def num_summary(dataframe, numerical_col, plot=False):
    # Define quantile values to be displayed
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    # Compute summary statistics
    summary = dataframe[numerical_col].describe(percentiles=quantiles)
    # Add median absolute deviation (MAD) to the summary statistics
    summary["mad"] = dataframe[numerical_col].mad()
    # Add skewness and kurtosis to the summary statistics
    summary["skewness"] = dataframe[numerical_col].skew()
    summary["kurtosis"] = dataframe[numerical_col].kurtosis()
    # Print the summary statistics
    print(summary)
    # Plot a histogram and a density plot for the numerical column (if plot=True)
    if plot:
        sns.histplot(dataframe[numerical_col], kde=True)
        plt.show()
        sns.kdeplot(dataframe[numerical_col])
        plt.show()

# Example usage of the num_summary function
num_summary(df, "age", plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)

# Capturing Variables and Generalizing Operations

# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# Load the titanic dataset and display first 5 rows and info
df = sns.load_dataset("titanic")
df.head()
df.info()

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    This function returns the names of categorical, numerical, and categorical-like cardinal variables in a dataset.
    
    Parameters
    ----------
    dataframe: dataframe
        The dataframe for which variable names are to be obtained.
    cat_th: int, float
        Class threshold value for numerical but categorical variables
    car_th: int, float
        Class threshold value for categorical-like cardinal variables

    Returns
    -------
    cat_cols: list
        List of categorical variables
    num_cols: list
        List of numerical variables
    cat_but_car: list
        List of categorical-like cardinal variables

    Notes
    ------
    cat_cols + num_cols + cat_but_car = total number of variables
    num_but_cat is within cat_cols.
    """

    # Categorical and categorical-like cardinal variables
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    # Numerical but categorical variables
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < 10 and dataframe[col].dtypes in ["int", "float"]]

    # Categorical-like cardinal variables
    cat_but_car = [col for col in dataframe.columns if
               dataframe[col].nunique() > 20 and str(dataframe[col].dtypes) in ["category", "object"]]

    # Combine the categorical and numerical but categorical variables, and exclude categorical-like cardinal variables
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # Numerical variables
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    # Display information about the dataset and the variables
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    # Return categorical, numerical, and categorical-like cardinal variable names
    return cat_cols, num_cols, cat_but_car

# Obtain the names of categorical, numerical, and categorical-like cardinal variables in the titanic dataset
cat_cols, num_cols, cat_but_car = grab_col_names(df)

# Function to summarize categorical columns in a pandas dataframe
def cat_summary(dataframe, col_name, plot=False):
    # Calculate value counts and percentages for the categorical column and print the results
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    # If plot is True, create a countplot of the categorical column
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


# Function to summarize numerical columns in a pandas dataframe
def num_summary(dataframe, numerical_col, plot=False):
    # Define the quantiles to be calculated for the numerical column
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    
    # Calculate summary statistics for the numerical column and print the results
    print(dataframe[numerical_col].describe(quantiles).T)

    # If plot is True, create a histogram of the numerical column
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


# Load the titanic dataset from Seaborn and display information about the dataframe
df = sns.load_dataset("titanic")
df.info()

# Convert boolean columns in the dataframe to integers
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

# Use a function to grab the names of categorical, numerical, and categorical-but-cardinal columns
cat_cols, num_cols, cat_but_car = grab_col_names(df)

# Summarize each categorical column in the dataframe using the cat_summary function
for col in cat_cols:
    cat_summary(df, col, plot=True)

# Summarize each numerical column in the dataframe using the num_summary function
for col in num_cols:
    num_summary(df, col, plot=True)

# 4. Anaysis of Target Variable

# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set display options for pandas dataframe
pd.set_option('display.max_columns', None) # Show all columns
pd.set_option('display.width', 500) # Set the width of the display

# Load the 'titanic' dataset from seaborn library
df = sns.load_dataset("titanic")

# Convert all boolean columns to integer columns
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

# Define a function called cat_summary
def cat_summary(dataframe, col_name, plot=False):
    # Print a summary table of the categorical variable
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    # Print a separator to separate the output from multiple function calls
    print("##########################################")

    # If the plot flag is True, create a countplot of the categorical variable
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

# Define a function called grab_col_names
def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    This function returns the names of categorical, numerical, and categorical but cardinal variables in the dataset.

    Parameters
    ----------
    dataframe: dataframe
        The dataframe for which variable names are to be obtained.
    cat_th: int, float
        Class threshold value for numerical but categorical variables
    car_th: int, float
        Class threshold value for categorical but cardinal variables

    Returns
    -------
    cat_cols: list
        List of categorical variables
    num_cols: list
        List of numerical variables
    cat_but_car: list
        List of categorical-looking cardinal variables

    Notes
    ------
    cat_cols + num_cols + cat_but_car = total number of variables
    num_but_cat is included in cat_cols.

    """
    # Determine categorical columns and categorical-looking numerical columns
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes in ["int", "float"]]

    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   str(dataframe[col].dtypes) in ["category", "object"]]

    # Combine categorical columns and categorical-looking numerical columns
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # Determine numerical columns
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    # Print the number of observations, variables, and each type of variable
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    # Return the lists of categorical, numerical, and categorical-looking cardinal variables
    return cat_cols, num_cols, cat_but_car

# Call the grab_col_names function with the input DataFrame df and store the output in the variables cat_cols, num_cols, and cat_but_car
cat_cols, num_cols, cat_but_car = grab_col_names(df)

# Display the first 5 rows of the DataFrame
df.head()

# Count the number of values for the "survived" column
df["survived"].value_counts()

# Call the cat_summary function 
cat_summary(df, "survived")

# Analysis of the Target Variable with Categorical Variables

# Calculate mean of 'survived' for each unique value of 'sex'
df.groupby("sex")["survived"].mean()

# Define a function to summarize the target variable based on categorical variables
def target_summary_with_cat(dataframe, target, categorical_col):
    # Calculate mean of 'target' for each unique value of 'categorical_col'
    summary_df = pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()})
    # Print the summary dataframe
    print(summary_df, end="\n\n\n")

# Call the function 'target_summary_with_cat' for each categorical column
# First, for column 'pclass'
target_summary_with_cat(df, "survived", "pclass")

# Then, for each column in 'cat_cols'
for col in cat_cols:
    target_summary_with_cat(df, "survived", col)


# Analysis of the Target Variable with Numerical Variables

# Calculate mean of 'age' for each value of 'survived'
df.groupby("survived")["age"].mean()

# Calculate mean of 'age' for each value of 'survived' using 'agg' function
df.groupby("survived").agg({"age":"mean"})

# Define a function to summarize the target variable based on numerical variables
def target_summary_with_num(dataframe, target, numerical_col):
    # Calculate mean of 'numerical_col' for each value of 'target'
    summary_df = dataframe.groupby(target).agg({numerical_col: "mean"})
    # Print the summary dataframe
    print(summary_df, end="\n\n\n")

# Call the function 'target_summary_with_num' for each numerical column
# First, for column 'age'
target_summary_with_num(df, "survived","age")

# Then, for each column in 'num_cols'
for col in num_cols:
    target_summary_with_num(df, "survived", col)

# 5. Correlation Analysis

# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set pandas display options to show all columns and increase width
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# Load the breast cancer dataset and select numerical columns
df = pd.read_csv("datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

# Get numerical column names
num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

# Calculate correlation matrix
corr = df[num_cols].corr()

# Set seaborn plot size and plot the correlation matrix as a heatmap
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

# Calculate absolute correlation matrix
cor_matrix = df.corr().abs()

# Get upper triangle of the correlation matrix
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))

# Get highly correlated variable names to drop
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col]>0.90)]

# Show the highly correlated variables and drop them from the dataset
cor_matrix[drop_list]
df.drop(drop_list, axis=1)

# Define a function to find highly correlated variables and drop them
def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list

# Apply the function to the breast cancer dataset
high_correlated_cols(df)

# Apply the function to the breast cancer dataset and plot the correlation matrix
drop_list = high_correlated_cols(df, plot=True)

# Drop the highly correlated variables from the breast cancer dataset
df.drop(drop_list, axis=1)

# Apply the function to the breast cancer dataset without highly correlated variables and plot the correlation matrix
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)

# Load a larger dataset related to fraud detection
df = pd.read_csv("datasets/fraud_train_transaction.csv")

# Apply the function to the fraud detection dataset and plot the correlation matrix
drop_list = high_correlated_cols(df, plot=True)

# Drop the highly correlated variables from the fraud detection dataset and show the number of remaining columns
len(df.drop(drop_list, axis=1).columns)



