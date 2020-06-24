import sys
import time
import display
import transform	
import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql

def privacy(db_name,query,mode):
    try:
        # Setup Connections
        connection = pg.connect(user = "postgres",password = "getup",host = "127.0.0.1",port = "5432",database = db_name)
        cursor = connection.cursor()
        query= query.lower()
        
        dtype=transform.find(query)
        
        if mode == "normal" or mode == "":# Normal Query 
            start_time = time.time()
            cursor.execute(query)
            end_time = time.time()

            record = cursor.fetchone()
            normal_time = (end_time-start_time)*1000
            return [record,normal_time]

        elif mode == 'bounded':# Differential Privacy with bounds
            tquery=transform.bounded(query,dtype)
            start_time = time.time()
            cursor.execute(tquery)
            end_time = time.time()

            record = cursor.fetchone()
            bounded_time = (end_time-start_time)*1000
            return [record, bounded_time]
        
        elif mode == "fastbounded":# Differential Privacy with fastbounds
            tquery=transform.fastbounded(query,dtype)
            start_time = time.time()
            cursor.execute(tquery)
            end_time = time.time()

            record = cursor.fetchone()
            fastbounded_time = (end_time-start_time)*1000
            return [record,fastbounded_time]

        elif mode=='winsorized':# Differential Privacy with winsorized bounds
            tquery=transform.winsorized(query,dtype)
            start_time = time.time()
            cursor.execute(tquery)
            end_time = time.time()

            record = cursor.fetchone()
            winsorized_time = (end_time-start_time)*1000
            return [record,winsorized_time]
        
        #return [normal_time,bounded_time,fastbounded_time,winsorized_time]


    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #Closing Connection.
            if(connection):
                cursor.close()
                connection.close()


