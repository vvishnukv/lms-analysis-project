import pandas as pd
import numpy as np
import random
from faker import Faker

# Set seed for reproducibility
np.random.seed(42)
fake = Faker()

print("Starting data generation...")

# 1. Generate 500 Courses
departments = ['Computer Science', 'Business', 'Liberal Arts', 'Science', 'Mathematics']
courses = pd.DataFrame({
    'course_id': range(101, 601),
    'department': np.random.choice(departments, 500),
    'accessibility_score': np.random.normal(75, 15, 500).clip(0, 100).astype(int), # Scores 0 to 100
})

# 2. Generate 10,000 Student Records linked to courses
num_students = 10000
student_course_ids = np.random.choice(courses['course_id'], num_students)

# Create a base dataframe
df = pd.DataFrame({
    'student_id': range(1, num_students + 1), 
    'course_id': student_course_ids
})
df = df.merge(courses, on='course_id')

# 3. Simulate Engagement and Grades (Intentionally correlating them with accessibility)
# Higher accessibility score slightly boosts engagement and grades
df['forum_posts'] = np.random.poisson(lam=(df['accessibility_score'] / 15))
df['video_watch_mins'] = np.random.normal(loc=(df['accessibility_score'] * 4), scale=45).clip(0).astype(int)

# Base grade + boost from accessibility + random noise
df['final_grade'] = (45 + (df['accessibility_score'] * 0.45) + np.random.normal(0, 8, num_students)).clip(0, 100)
df['final_grade'] = df['final_grade'].round(1)

# 4. Export to CSV
file_name = 'lms_accessibility_data.csv'
df.to_csv(file_name, index=False)

print(f"Success! {num_students} records generated and saved to {file_name}")
print(df.head()) # Show the first 5 rows in the terminal