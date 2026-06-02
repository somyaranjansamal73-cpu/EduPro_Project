import pandas as pd

# Load datasets
users = pd.read_csv("users.csv")
courses = pd.read_csv("courses.csv")
transactions = pd.read_csv("transactions.csv")

print("Total Users:", len(users))
print("Total Courses:", len(courses))
print("Total Transactions:", len(transactions))

print("\nCourse Enrollments:")
print(transactions["CourseID"].value_counts())
print("\nMost Popular Course:")
print(transactions["CourseID"].value_counts().idxmax())
# Age Groups
users["AgeGroup"] = pd.cut(
    users["Age"],
    bins=[0,18,25,35,45,100],
    labels=["<18","18-25","26-35","36-45","45+"]
)

print("\nAge Group Distribution:")
print(users["AgeGroup"].value_counts())
print("\nGender Distribution:")
print(users["Gender"].value_counts())
merged = transactions.merge(courses, on="CourseID")

print("\nCourse Category Popularity:")
print(merged["CourseCategory"].value_counts())
import matplotlib.pyplot as plt

# Age Group Chart
users["AgeGroup"].value_counts().plot(kind="bar")

plt.title("Age Group Distribution")
plt.xlabel("Age Groups")
plt.ylabel("Number of Users")

plt.show()
# Gender Distribution Chart

import matplotlib.pyplot as plt

users["Gender"].value_counts().plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Users")

plt.show()
# Course Category Pie Chart

merged["CourseCategory"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Course Category Popularity")

plt.show()
