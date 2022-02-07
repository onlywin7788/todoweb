import pymysql
import pandas as pd

class TodoList:

    def __init__(self):
        self.db = None
        self.cursor = None

    def initialize(self):
        pass

    def connect(self):
        self.db = pymysql.connect(
            user='root',
            passwd='mococo1$',
            host='127.0.0.1',
            db='todo_web',
            charset='utf8'
        )

    def open(self):
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def select(self, sql):

##        sql = "SELECT * FROM `todo`;"


        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    def close(self):
        pass

    def disconnect(self):
        pass

    def unitialize(self):
        pass