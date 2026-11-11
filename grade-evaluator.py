import csv
import sys
import os
import math

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ").strip() # i used strip to clean up any whitespace I might have in my code.
    
    if not filename:
        print("Error: Please provide a CSV filename.")
        sys.exit(1)

    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' doesn't exist.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            requiredColumns = ['assignment', 'group', 'score', 'weight']
            if reader.fieldnames is None:
                print("Error: The CSV file is empty.")
                sys.exit(1)
            
            for col in requiredColumns:
                if col not in reader.fieldnames:
                    print(f"Error: {col} column is missing from the CSV.")
                    sys.exit(1)

            for lineNo, row in enumerate(reader, start=2):
                if not all(row.get(col) and row[col].strip() for col in requiredColumns):
                    print(f"Error: We found a missing data in row {lineNo}: {row}")
                    sys.exit(1)

                try:
                    score = float(row['score'])
                    weight = float(row['weight'])
                except ValueError:
                    print(f"Error: Invalid numeric value in row {lineNo}: {row}")
                    sys.exit(1)
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': score,
                    'weight': weight
                })

                # i also added a check to handle the case where the assignment does not exist.
                if not assignments:
                    print("Error: The CSV file doesn't have any assignments.")
                    sys.exit(1)
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    
    # did .... a) Check if all scores are percentage based (0-100)
    
    for assignment in data:
        score = assignment['score']

        if not(0 <= score <= 100):

            print(f"Error: Invalid score for assignment '{assignment['assignment']}'. It is out of range (0-100): {score}")
            sys.exit(1)

        if assignment['group'] not in [ 'Formative', 'Summative']:
            print(f"Error: Invalid group for assignment '{assignment['assignment']}'. It should be either 'Formative' or 'Summative'.")
            sys.exit(1)
    print("All scores are valid and are between (0-100).")
    # done with :) b) Validate total weights (Total=100, Summative=40, Formative=60)
    
    formative =  0.0
    summative = 0.0

    for assignment in data:
        weight = assignment['weight']

        if not (0 <= weight <= 100):
            print(f"Error: Invalid weight {weight} for assignment '{assignment['assignment']}'. It is out of range (0-100): {weight}")
            sys.exit(1)
        if assignment['group'] == 'Formative':
            formative += weight
        elif assignment['group'] == 'Summative':
            summative += weight
    total = formative + summative
    if not math.isclose(total, 100.0, rel_tol=0, abs_tol=1e-9):
        print(f"Error: The total weight is {total}, but it should be 100.")
        sys.exit(1)

# Check the formative weight
    if not math.isclose(formative, 60.0, rel_tol=0, abs_tol=1e-9):
        print(f"Error: The total formative weight is {formative}, but it should be 60.")
        sys.exit(1)

    # Check the summative weight
    if not math.isclose(summative, 40.0, rel_tol=0, abs_tol=1e-9):
        print(f"Error: The total summative weight is {summative}, but it should be 40.")
        sys.exit(1)

    #  c) Calculate the Final Grade and GPA
    total_grade = 0.0

    for assignment in data:
        score = assignment['score']
        weight = assignment['weight']

        contribution = (score * weight) / 100
        total_grade += contribution
    Gpa = (total_grade / 100) * 5.0

    
    print (f"\nFinal Grade: {FinalGrade:.2f}%")
    print (f"GPA: {Gpa:.2f} / 5.00")
    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
    
    pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)