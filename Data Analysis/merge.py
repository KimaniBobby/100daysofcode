import pandas as pd

# Create a sample data frame
df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [10, 20, 30, 40],
                   'C': [100, 200, 300, 400]})

# Display the initial data frame
print("Initial data frame:")
print(df)

# Define the data to add
new_data = {'A': [2, 4], 'D': [2000, 4000]}

# Convert the data to a data frame
new_df = pd.DataFrame(new_data)

# Iterate through the rows of the new data frame
for index, row in new_df.iterrows():
    # Check if the value in the first column matches any value in the 'A' column of the initial data frame
    if row['A'] in df['A'].values:
        # Get the index of the row in the initial data frame where the first column matches the value in the new data frame
        row_index = df[df['A'] == row['A']].index[0]
        # Add the value from the new data frame to the corresponding row and column in the initial data frame
        df.at[row_index, 'D'] = row['D']

# Display the updated data frame
print("\nData frame after adding values:")
print(df)
