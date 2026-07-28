import os

import pyodbc

from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    """Handles SQL Server database connections."""
    def __init__(self):
        self.server = os.getenv("SERVER")
        self.database = os.getenv("DATABASE")
        self.driver = os.getenv("DRIVER")
        self.trusted_connection = os.getenv("TRUSTED_CONNECTION")

    def get_connection(self):
        connection_string = (
        f"DRIVER={{{self.driver}}};"
        f"SERVER={self.server};"
        f"DATABASE={self.database};"
        f"Trusted_Connection={self.trusted_connection};"
    )
    
        return pyodbc.connect(connection_string)

    def test_connection(self):
        try:
            conn = self.get_connection()

            # print("Connected successfully!")
            return True
            

            conn.close()

        except Exception as e:
            print(e)