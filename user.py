import sqlite3

class User:
 def __init__(self,id,username,password):
  self.id=id
  self.username=username
  self.password=password

  @classmethod
  def findby_username(cls,username):
      connection = sqlite3.connect("data.db")
      cursor=connection.cursor()
      query="select * from users where username=?"
      result=cursor.execute(query,(username,))
      row=result.fetchone()
      if row:
          user=cls(row[0],row[1],row[2])
      connection.close()
      return row

  @classmethod
  def findby_id(cls,id):
      connection = sqlite3.connect("data.db")
      cursor = connection.cursor()
      query = "select * from users where id=?"
      result = cursor.execute(query, (id,))
      row = result.fetchone()
      if row:
          user = cls(row[0], row[1], row[2])
      connection.close()
      return row





