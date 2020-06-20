import psycopg2 as pg 
import time
import sys
import pandas as pd
import math
import numpy as np
#import matplotlib.pyplot as plt

try:
#connections to the database
    connection = pg.connect(user = 'postgres', password = "password", host = "127.0.0.1",port = "5432",database = "uber")
    cursor = connection.cursor()

    #test queries
    query = ["SELECT AVG(total_distance) FROM completeride", "SELECT COUNT(*) FROM passenger","SELECT AVG(working_hours) FROM DRIVER"]

    test = {'query':[],'result': [],'time_taken':[]} 

    #time

    for i in query:
        testing_time = []
        result = 0
        for j in range(10):
            start = time.time()
            cursor.execute(i)
            result = cursor.fetchall()
            end = time.time()
            exec_time = (end - start)*1000
            testing_time.append(exec_time)

        #func = i.split("(")[0][7:]
        test['query'].append(i)
        test['result'].append(result[0][0])
        test['time_taken'].append(np.mean(testing_time))

    #print(test)
    df = pd.DataFrame(test)
    print(df.head())



except Exception as e:
    print("Unable to connect to PostgreSQL server: ",e)
