# -*- coding: utf-8 -*-
import  sqlite3

class sqliteHelp(object):
    DB_SQLITE_NAME="sour.db"
    sqlite_conn=sqlite3.connect(DB_SQLITE_NAME)
    sqlite_cursor=sqlite_conn.cursor()

    def __init__(self):
        self=self

    def sqliteExecute(self,sql):
        if len(sql)>0:
            self.sqlite_cursor.execute(sql)
            self.sqlite_conn.commit()

    def creatTable(self):
        sql1="DROP TABLE IF EXISTS main.Introduction;"
        self.sqliteExecute(sql1)
        sql="CREATE TABLE Introduction (name  TEXT,countries  TEXT,season  TEXT,url  TEXT,Iid  TEXT,resources  TEXT);"
        self.sqlite_cursor.execute(sql)
        self.sqlite_conn.commit()