import pandas as pd
from database.connection import DatabaseConnection
from typing import Sequence,Any


class Repository:
    def __init__(self):
        self.db = DatabaseConnection()

    def fetch_dataframe(self,query:str)->pd.DataFrame:
        conn=None
        try:
            conn=self.db.get_connection()
            df=pd.read_sql_query(query,conn)
            return df
        
        finally:
            if conn:
                conn.close()

    def execute(self,query:str)->None:
        conn=None
        cursor=None
        try:
            conn=self.db.get_connection()
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
                print(f"Error:{e}")
                raise 
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def fetch_scalar(self,query:str)->Any:
        conn=None
        cursor=None
        try:
            conn=self.db.get_connection()
            cursor=conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            if result is None:
                return None
            return result[0]
 
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def execute_many(self,query:str,params:Sequence[Sequence[Any]])->None:
        conn=None
        cursor=None
        try:
            conn=self.db.get_connection()
            cursor=conn.cursor()
            cursor.executemany(query,params)
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
                print(f"Error:{e}")
                raise 
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            
            

