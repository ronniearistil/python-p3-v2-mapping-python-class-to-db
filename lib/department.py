from __init__ import CURSOR, CONN  # Import the database connection (CONN) and cursor (CURSOR) for executing SQL commands.

class Department:
    # Define the Department class, representing departments in the database.

    def __init__(self, name, location, id=None):
        # Initialize a Department instance with a name, location, and optional id (defaults to None).
        self.id = id  # Unique identifier for the department, assigned upon saving to the database.
        self.name = name  # Name of the department (e.g., "HR").
        self.location = location  # Location of the department (e.g., "Building C, East Wing").

    def __repr__(self):
        # Return a string representation of the Department object for easy viewing.
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        # Class method to create the 'departments' table in the database, if it doesn't already exist.
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)  # Execute the SQL command to create the table.
        CONN.commit()  # Commit the transaction to save changes in the database.

    @classmethod
    def drop_table(cls):
        # Class method to delete the 'departments' table from the database.
        sql = "DROP TABLE IF EXISTS departments;"
        CURSOR.execute(sql)  # Execute the SQL command to drop the table.
        CONN.commit()  # Commit the transaction to save changes.

    def save(self):
        # Instance method to save the department as a new row in the 'departments' table.
        sql = "INSERT INTO departments (name, location) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.location))  # Insert name and location into the table.
        CONN.commit()  # Commit the transaction to save changes.
        self.id = CURSOR.lastrowid  # Set the instance's id attribute to the primary key of the new row.

    @classmethod
    def create(cls, name, location):
        # Class method to create and save a new Department instance in a single step.
        department = cls(name, location)  # Initialize a new Department object.
        department.save()  # Save the department to the database.
        return department  # Return the saved Department instance.

    def update(self):
        # Instance method to update the row in the 'departments' table that matches this instance's id.
        sql = "UPDATE departments SET name = ?, location = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.location, self.id))  # Update the table with current name, location.
        CONN.commit()  # Commit the transaction to save changes.

    def delete(self):
        # Instance method to delete the row in the 'departments' table that matches this instance's id.
        sql = "DELETE FROM departments WHERE id = ?"
        CURSOR.execute(sql, (self.id,))  # Delete the row matching the id.
        CONN.commit()  # Commit the transaction to save changes.

