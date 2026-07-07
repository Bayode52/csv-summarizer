import csv
import os

#path to your CSV file
file_path = r"C:\Users\bayod\OneDrive\Desktop\expenses.csv"
#check if file exists before trying to open it
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    with open(file_path,"r") as file:
        reader = csv.reader(file)
        # Grab the first row (column names)
        headers = next (reader)
        print(f"Column names: {headers}")
        #convert all remaining rows into a list
        rows = list(reader) 
        print(f"Total rows(excluding header): {len(rows)}")
        #Fnd which columns contains numbers
        #check the first data row to identify numeric columns
        numeric_cols = []
        if rows:
            first_row = rows[0]
            for i, value in enumerate(first_row):
                try:
                    float(value)
                    numeric_cols.append(i)
                except ValueError:
                    pass #Not a number, skip it

        #for each numeric column, calculate stats
        for col_index in numeric_cols:
            col_name = headers[col_index]
            values = []
            for row in rows:
                try:
                    values.append(float(row[col_index]))
                except (ValueError, IndexError):
                    pass #Skip rows where this column isn't a number
            if values:
                total = sum(values)
                average = total / len(values)
                maximum = max(values)
                minimum = min(values)
                print(f"\nStats for '{col_name}':")
                print(f" Sum: {total:.2f}")
                print(f" Average: {average:.2f}")
                print(f" Min: {minimum:.2f}")
                print(f" Max: {maximum:.2f}")
