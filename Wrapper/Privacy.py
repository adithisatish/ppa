import sys
import time
import display
import transform	
import psycopg2 as pg
import pandas as pd
import pandas.io.sql as psql

def display_output(result):
    #l = len(result)
    for i in result:
        for j in i:
            print(j,sep = " | ")
        print("\n",end = "")

try:
    # Setup Connections
    connection = pg.connect(user = "postgres",password = "getup",host = "127.0.0.1",port = "5432",database = str(sys.argv[1]))
    cursor = connection.cursor()
    query= sys.argv[2] #.lower()
    
    dtype=transform.find(query)
    
    # Normal Query 
    start_time = time.time()
    cursor.execute(query)
    end_time = time.time()

    record = cursor.fetchall()
    print("Normal\n-----------\n")
    print("Result : ")
    display_output(record)
    normal_time = (end_time-start_time)*1000
    print("----------\nExecution Time : ",normal_time,"ms")
    print("----------------\n\n")
    '''start_time = time.time()
    cursor=pd.read_sql_query(query,connection)
    cursor= psql.read_sql(query, connection)
    end_time = time.time()
    l=len(cursor.columns)
    a=cursor[cursor.columns[0:l]].values.tolist()
    #for col in cursor.columns:
        #print(col,end=" ")
    n=len(a)
    print("\n")
    for i in a:
        j=0
        m=len(i)
        while(j<m):
            print(i[j],end=" ")
            j=j+1
        print("\n")    
    #record = cursor.fetchall()
    #display.log("Normal",end_time-start_time,dtype,record)
    #display.log("Normal",end_time-start_time,dtype,cursor)'''

    # Differential Privacy with bounds
    tquery=transform.bounded(query,dtype)
    start_time = time.time()
    cursor.execute(tquery)
    end_time = time.time()
    #print(tquery)
    record = cursor.fetchall()
    print("Bounded\n-----------\n")
    print("Result : ")
    display_output(record)
    bounded_time = (end_time-start_time)*1000
    print("----------\nExecution Time : ",bounded_time,"ms")
    print("----------------\n\n")
    '''start_time = time.time()
    #cursor.execute(tquery)
    cursor=pd.read_sql_query(tquery,connection)
    display.log("Bounded",dtype,cursor)
    cursor= psql.read_sql(tquery, connection,None)
    end_time = time.time()
    #record = cursor.fetchall()
    #display.log("Bounded",end_time-start_time,dtype,record)
    l=len(cursor.columns)
    a=cursor[cursor.columns[0:l]].values.tolist()
    for col in cursor.columns:
        print(col,end=" ")
    n=len(a)
    print("\n")
    for i in a:
        j=0
        m=len(i)
        while(j<m):
            print(i[j],end=" ")
            j=j+1
        print("\n")
    #display.log("Bounded",end_time-start_time,dtype,cursor)'''
    
    # Differential Privacy with fastbounds
    tquery=transform.fastbounded(query,dtype)
    start_time = time.time()
    cursor.execute(tquery)
    end_time = time.time()
    #print(tquery)
    record = cursor.fetchall()
    print("Fast Bounded\n-----------\n")
    print("Result : ")
    display_output(record)
    fastbounded_time = (end_time-start_time)*1000
    print("----------\nExecution Time : ",fastbounded_time,"ms")
    print("----------------\n\n")
    '''print(tquery)
    start_time = time.time()
    #cursor.execute(tquery)
    cursor=pd.read_sql_query(tquery,connection)
    display.log("FastBounded",dtype,cursor)
    cursor= psql.read_sql(tquery, connection,None)
    end_time = time.time()
    record = cursor.fetchall()
    l=len(cursor.columns)
    a=cursor[cursor.columns[0:l]].values.tolist()
    for col in cursor.columns:
        print(col,end=" ")
    n=len(a)
    print("\n")
    for i in a:
        j=0
        m=len(i)
        while(j<m):
            print(i[j],end=" ")
            j=j+1
        print("\n")
    #display.log("FastBounded",end_time-start_time,dtype,record)
    #display.log("FastBounded",end_time-start_time,dtype,cursor)'''

    # Differential Privacy with winsorized bounds
    tquery=transform.winsorized(query,dtype)
    start_time = time.time()
    cursor.execute(tquery)
    end_time = time.time()
    #print(tquery)
    record = cursor.fetchall()
    print("Widened Winsorized Bounds\n-----------\n")
    print("Result : ")
    display_output(record)
    winsorized_time = (end_time-start_time)*1000
    print("----------\nExecution Time : ",winsorized_time,"ms")
    print("----------------\n\n")
    
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #Closing Connection.
        if(connection):
            cursor.close()
            connection.close()
