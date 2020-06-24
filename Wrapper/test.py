import Privacy
import display
import transform
import psycopg2 as pg
import time
import sys
import os

cwd = os.getcwd().split("/") #change to "/" in Linux
del(cwd[-1])
file_path = "/".join(cwd) + "/queries.txt"

