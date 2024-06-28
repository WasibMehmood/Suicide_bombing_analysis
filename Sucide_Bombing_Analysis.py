import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'Suicide_bombing_attacks.csv'  # replace with the correct file path
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Preprocess the data
# Convert date columns to datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data['Islamic Date'] = pd.to_datetime(data['Islamic Date'], errors='coerce')

# Convert 'Killed Min', 'Killed Max', 'Injured Min', 'Injured Max' to numeric values
data['Killed Min'] = pd.to_numeric(data['Killed Min'], errors='coerce').fillna(0)
data['Killed Max'] = pd.to_numeric(data['Killed Max'], errors='coerce').fillna(0)
data['Injured Min'] = pd.to_numeric(data['Injured Min'], errors='coerce').fillna(0)
data['Injured Max'] = pd.to_numeric(data['Injured Max'], errors='coerce').fillna(0)

# Add year and month columns for trend analysis
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month

# Basic statistics
print(data.describe())

# Frequency of attacks over time
plt.figure(figsize=(14, 7))
sns.countplot(x='Year', data=data)
plt.title('Number of Suicide Bombing Attacks per Year')
plt.xticks(rotation=45)
plt.show()

# Attacks by city
plt.figure(figsize=(14, 7))
data['City'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Cities with Most Suicide Bombing Attacks')
plt.show()

# Attacks by province
plt.figure(figsize=(14, 7))
data['Province'].value_counts().plot(kind='bar')
plt.title('Number of Suicide Bombing Attacks by Province')
plt.show()

# Casualties analysis
plt.figure(figsize=(14, 7))
sns.lineplot(x='Year', y='Killed Max', data=data, label='Max Killed', color='red')
sns.lineplot(x='Year', y='Injured Max', data=data, label='Max Injured', color='blue')
plt.title('Casualties Over Time')
plt.legend()
plt.show()

# Location category analysis
plt.figure(figsize=(14, 7))
data['Location Category'].value_counts().plot(kind='bar')
plt.title('Number of Suicide Bombing Attacks by Location Category')
plt.show()

# Target type analysis
plt.figure(figsize=(14, 7))
data['Target Type'].value_counts().plot(kind='bar')
plt.title('Number of Suicide Bombing Attacks by Target Type')
plt.show()

# Heatmap of attacks by location
plt.figure(figsize=(14, 7))
sns.scatterplot(x='Longitude', y='Latitude', hue='Killed Max', size='Killed Max', sizes=(20, 200), data=data)
plt.title('Geographical Distribution of Suicide Bombing Attacks')
plt.show()