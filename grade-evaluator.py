import csv
import sys
import os

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
    
    # TODO: a) Check if all scores are percentage based (0-100)
    
    for assignment in data:
        score = assignment['score']

        if not(0 <= score <= 100):

            print(f"Error: Invalid score for assignment '{assignment['assignment']}'. It is out of range (0-100): {score}")
            sys.exit(1)
    print("All scores are valid and are between (0-100).")

    if assignment['group'] not in [ 'Formative', 'Summative']:
        print(f"Error: Invalid group for assignment '{assignment['assignment']}'. It should be either 'Formative' or 'Summative'.")
        sys.exit(1)
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    # TODO: c) Calculate the Final Grade and GPA
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