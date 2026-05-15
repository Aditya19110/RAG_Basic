import pandas as pd
import os

# Create folder
os.makedirs("../data/csv_files", exist_ok=True)

# Sample data
employees_data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikram"],
    "Department": ["AI", "HR", "Engineering", "Marketing", "Finance"],
    "Experience": [2, 5, 3, 4, 6],
    "Salary": [50000, 65000, 72000, 58000, 81000]
}

# Create DataFrame
df = pd.DataFrame(employees_data)

# Save CSV
csv_path = "../data/csv_files/employees.csv"
df.to_csv(csv_path, index=False)

print(f"CSV file created at: {csv_path}")

# Preview
print(df)