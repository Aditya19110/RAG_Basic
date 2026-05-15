import pandas as pd
import os

# Create folder
os.makedirs("data/excel_files", exist_ok=True)

# Sample student data
students_data = {
    "StudentID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikram"],
    "Course": ["AI", "Data Science", "Python", "RAG", "ML"],
    "Marks": [85, 92, 78, 88, 95],
    "City": ["Pune", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]
}

# Create DataFrame
df = pd.DataFrame(students_data)

# Excel file path
excel_path = "data/excel_files/students.xlsx"

# Save Excel file
df.to_excel(excel_path, index=False)

print(f"Excel file created successfully at: {excel_path}")

# Preview
print(df)