# Description: Script to fetch course data from the NYU API and save it as JSON and CSV files.
import requests
import json
import csv
import pandas as pd

# Base URL from the API
BASE_URL = "https://nyu.a1liu.com"

# Function to fetch course data
def fetch_courses(term, subject):
    endpoint = f"{BASE_URL}/api/courses/{term}/{subject}"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {endpoint}: {e}")
        return []

# Function to save as JSON
def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename} (JSON)")

# Function to save as CSV
def save_to_csv(data, filename):
    # Flattening nested data for CSV compatibility
    flat_data = []
    for course in data:
        for section in course.get("sections", []):
            flat_data.append({
                "Course Name": course.get("name", ""),
                "Department Course ID": course.get("deptCourseId", ""),
                "Description": course.get("description", ""),
                "Section Name": section.get("name", ""),
                "Section Type": section.get("type", ""),
                "Registration Number": section.get("registrationNumber", ""),
                "Instructors": ", ".join(section.get("instructors", [])),
                "Campus": section.get("campus", ""),
                "Location": section.get("location", "")
            })
    # Convert to CSV
    df = pd.DataFrame(flat_data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename} (CSV)")

# Main logic
if __name__ == "__main__":
    # Replace these with appropriate values
    term = "fa2022"  # Example term
    subjects = ["MATH-UA", "CSCI-UA"]  # Example subjects

    all_courses = []
    for subject in subjects:
        courses = fetch_courses(term, subject)
        all_courses.extend(courses)

    # Save data
    save_to_json(all_courses, "static\courses.json")
    save_to_csv(all_courses, "static\courses.csv")