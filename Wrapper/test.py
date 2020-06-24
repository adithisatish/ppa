import Privacy
import os

path = os.getcwd().split("/") #change to "/" in Linux
del(path[-1])
print("/".join(path) + "/queries.txt")
