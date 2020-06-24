from test_privacy import privacy
import display
import transform
import psycopg2 as pg
import time
import sys
import os
import pandas as pd 
import numpy as np

def isstr(s):
    try:
        s.lower()
        return True
    except:
        return False

def exec_query(query,mode):
    time = []
    result = []
    for i in range(56):
        val = privacy("uber",query,mode)
        time.append(val[1])
        result.append(val[0])
    
    avg_time = sum(time)/56
    if None in result:
        avg_result = None
    elif isstr(result[0]):
        avg_result = None
    else:
        avg_result = sum(result)/56
    
    return [avg_result,avg_time]


cwd = os.getcwd().split("/") #change to "/" in Linux
del(cwd[-1])
file_path = "/".join(cwd) + "/queries.txt"

file = open(file_path,'r')
queries = file.readlines()

norm = {"query":[],"result":[],"exec_time":[]}
bound =  {"query":[],"result":[],"exec_time":[]}
fbnded =  {"query":[],"result":[],"exec_time":[]}
win =  {"query":[],"result":[],"exec_time":[]}

for i in queries:
    norm["query"].append(i)
    normal = exec_query(i,"normal")
    norm["result"].append(normal[0])
    norm["exec_time"].append(normal[1])

    bound["query"].append(i)
    bounded = exec_query(i,"bounded")
    bound["result"].append(bounded[0])
    bound["exec_time"].append(bounded[1])

    fbnded["query"].append(i)
    fastbounded = exec_query(i,"fastbounded")
    fbnded["result"].append(fastbounded[0])
    fbnded["exec_time"].append(fastbounded[1])

    win["query"].append(i)
    winsorized = exec_query(i,"winsorized")
    win["result"].append(winsorized[0])
    win["exec_time"].append(winsorized[1])

df_normal = pd.DataFrame(norm)
print("\nNORMAL\n",df_normal.head(10))
print("\n-------------------------------------------------\n")

df_bound = pd.DataFrame(bound)
print("\nBOUNDED\n",df_bound.head(10))
print("\n-------------------------------------------------\n")

df_fastbound = pd.DataFrame(fbnded)
print("\nFAST BOUNDED\n",df_fastbound.head(10))
print("\n-------------------------------------------------\n")

df_winsorized = pd.DataFrame(win)
print("\nWIDENED WINSORIZED\n",df_winsorized.head(10))
print("\n-------------------------------------------------\n")




file.close()
