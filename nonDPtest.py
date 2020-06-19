import psycopg2 as pg 
import time
import sys
import pandas as pd

try:
#connections to the database
    connection = pg.connect(user = 'postgres', password = "dbmssem4", host = "127.0.0.1",port = "5432",database = "uber") ##IMPORTANT: change password to 'password' before running in the lab system
    cursor = connection.cursor()
    #sample query
    query = "SELECT AVG(total_distance) FROM completeride"
    #time
    start = time.time()
    cursor.execute(query)
    result = cursor.fetchall()
    end = time.time()
    print("Result : ",result[0][0])
    print("Time: ",(end-start)*1000, "ms")

except Exception as e:
    print("Unable to connect to PostgreSQL server {e}")
