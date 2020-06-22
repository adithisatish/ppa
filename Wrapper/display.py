l=15
empty=""
def log(query,time,dtype,record = None):
	print("Query: "+query)
	print(dtype.center(l))
	print(empty.center(l,"-"))
	try:
		if(record[0]):
				print(str(float(record[0])).center(l))
	except:
		print("")
	print("Time Taken:" + str(time*1000)+"ms")
