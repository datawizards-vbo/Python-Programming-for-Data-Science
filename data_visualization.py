import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a DataFrame
data = pd.read_csv("my_data.csv")

# Create a line plot
plt.plot(data["column1"], data["column2"])
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Line plot")
plt.show()

# Create a scatter plot
plt.scatter(data["column1"], data["column2"])
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Scatter plot")
plt.show()

# Create a histogram using seaborn
sns.histplot(data["column1"])
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Histogram")
plt.show()

# Create a box plot using seaborn
sns.boxplot(x="column1", y="column2", data=data)
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Box plot")
plt.show()

# Create a violin plot using seaborn
sns.violinplot(x="column1", y="column2", data=data)
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Violin plot")
plt.show()

# Create a heatmap using seaborn
sns.heatmap(data.corr(), annot=True)
plt.title("Heatmap")
plt.show()


