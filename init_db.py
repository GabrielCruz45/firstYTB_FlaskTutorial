from app import create_app, db
from sqlalchemy.exc import SQLAlchemyError

app = create_app()

try:
    with app.app_context(): # The .app_context() method creates a temporary environment where your code 
        # can access the application's settings and extensions.
        db.create_all()
        print("Database was successfully created")
except SQLAlchemyError as e:
    print(f"An error occured when creating the table. {e}")
except Exception as e:
    print(f"An unexpected error occured {e}")



# Other type of example of with statement (not being used as file opening/closing/error handling)

# import sqlite3

# with sqlite3.connect("example.db") as conn:
    
#     cursor = conn.cursor()
#     cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
#     res = cursor.fetchone()
#     print("Table created successfully!" if res else "Table not found."