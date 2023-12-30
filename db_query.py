import sqlite3

def delete_all_records(database_path, table_name):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()

        # Delete all records from the specified table
        cursor.execute(f"DELETE FROM {table_name};")

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        print(f"All records deleted from {table_name} successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting records: {e}")

# Example usage:
database_path = "db.sqlite3"
table_name = input("Table name: ")
delete_all_records(database_path, table_name)
