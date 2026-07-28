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

    def _build_connection_string(self):
        connection_string = (
        f"DRIVER={{{self.driver}}};"
        f"SERVER={self.server};"
        f"DATABASE={self.database};"
        f"Trusted_Connection={self.trusted_connection};"
    )
        return connection_string

    def get_connection(self):
        return pyodbc.connect(self._build_connection_string())
        

    def test_connection(self):
        try:
            with self.get_connection():
                return True
        except Exception as e:
            print(e)
            return False