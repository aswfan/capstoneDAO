# coding=utf-8
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};' 
                      + 'Server=bulubulu.ischool.uw.edu, 11433;'
                      + 'Database=YVYC;'
                      + 'uid=sa;pwd=GoTeam2018!')

cursor = conn.cursor()
sql = 'select * from proposal.draft_proposal'

cursor.execute(sql)
result = cursor.fetchone()

print(result)

conn.close()