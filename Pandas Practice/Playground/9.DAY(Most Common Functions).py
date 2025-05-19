import pandas as pd

# Read CSV, Excel, JSON
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")




df.head()        # First 5 rows
df.tail()        # Last 5 rows
df.shape         # (rows, columns)
df.columns       # Column names
df.info()        # Data types and non-null counts
df.describe()    # Stats for numeric columns




df['col']               # Select column
df[['col1', 'col2']]    # Multiple columns
df.iloc[0]              # Row by index
df.loc[0, 'col']        # Cell by label

df[df['col'] > 10]      # Conditional filtering
df[(df['a'] > 0) & (df['b'] < 100)]  # Multiple conditions



df.isna()              # Where data is missing
df.isna().sum()        # Count missing per column
df.dropna()            # Drop rows with any NaNs
df.fillna(0)           # Replace NaNs with 0




df['col'].astype(int)               # Convert type
df.rename(columns={'a':'A'})        # Rename column
df['new'] = df['a'] + df['b']       # Create new column
df['col'] = df['col'].str.lower()   # String ops





df.sort_values('col', ascending=False)
df['rank'] = df['score'].rank()




df['col'].value_counts()       # Frequency count
df['col'].unique()             # Unique values
df['col'].duplicated()         # Detect duplicates
df.duplicated().sum()          # Number of duplicate rows
df.drop_duplicates()           # Remove duplicates


