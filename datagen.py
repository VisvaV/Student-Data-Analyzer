import pandas as pd
import numpy as np

# Define the number of rows for the dataset
num_rows = 1000

# Generate random data for the dataset
data = {
    'Name': [f'Student {i}' for i in range(1, num_rows + 1)],
    'Roll No': np.random.randint(1, 100, size=num_rows),
    'Subject': np.random.choice(['Mathematics', 'Science', 'History', 'English'], size=num_rows),
    'Cont Asses 1': np.random.randint(10, 21, size=num_rows),
    'Cont Asses 2': np.random.randint(10, 21, size=num_rows),
    'Tutorial Marks': np.random.randint(10, 21, size=num_rows),
    'Student Attendance': np.random.randint(20, 31, size=num_rows),
    "Teacher's Name": np.random.choice(['Mr. Smith', 'Miss Johnson', 'Dr. Brown', 'Mrs. White'], size=num_rows)
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('large_dataset.csv', index=False)

print("Large dataset saved as large_dataset.csv")
