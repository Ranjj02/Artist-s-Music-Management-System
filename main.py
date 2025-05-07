import tkinter as tk
import mysql.connector

def create_table():
    # Establish a connection to the MySQL server
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="music"
    )

    # Create a cursor object
    cursor = db.cursor()

    # SQL query to create a table
    create_table_query = """
    CREATE TABLE Employees (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(40),
        Age INT,
        Gender VARCHAR(10),
        Salary FLOAT
    )
    """

    # Execute the query
    cursor.execute(create_table_query)

    # Close the connection
    db.close()

# Create a Tkinter window
root = tk.Tk()

# Create a button that calls the 'create_table' function when clicked
button = tk.Button(root, text="Create Table", command=create_table)
button.pack()

# Run the Tkinter event loop
root.mainloop()
