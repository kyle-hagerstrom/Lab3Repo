import pandas as pd
import sys

# Code ensures the script receives a filename as an argument
if len(sys.argv) < 2:
    print("Usage: python python_csv_cleaner.py <input_csv_file>")
    sys.exit(1)

#User provided csv file
input_file = sys.argv[1]

#Output file name
output_file = "cleaned_" + input_file

# Load CSV into DataFrame
df = pd.read_csv(input_file)

# Print initial row count 
print("Initial row count:\n",df.count())

# Remove rows with missing values
df.dropna(inplace=True)

# Print row count after removing missing values
print("After removing missing values:\n",df.count())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Print row count after removing duplicates
print("After removing duplicates:\n",df.count())

# Save cleaned data to a new CSV file
df.to_csv(output_file, index=False)

print("Cleaned CSV saved as:", output_file)
