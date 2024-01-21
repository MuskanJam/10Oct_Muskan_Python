from tkinter import NO
import pymysql

class Database:
  def __init__(self):
    self.connection = pymysql.connect(host='localhost', user='root', password='', database='productdata')
    self.cursor = self.connection.cursor()

  def execute_query(self, query, values=None):
    try:
      self.cursor.execute(query, values)
      self.connection.commit()
      return True
    except Exception as e:
      print(f"Error: {e}")
      self.connection.rollback()
      return False
    
  def fetch_data(self, query,values=None):
    try:
      if values:
        self.cursor.execute(query, values)
      else:
        self.cursor.execute(query)
      data = self.cursor.fetchall()
      return data
    except Exception as e:
      print(f"Error: {e}")
      return None