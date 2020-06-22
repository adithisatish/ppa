
#Function to idetify type
def find(query):
	lst=query.split("from")[0]
	types=["count","sum","avg","var","stdev"]	
	for i in types:
		if (i+"(") in lst:
			return i
	return "default"

#Function which returns transformed Bounded Query
def bounded(query,dtype):
	if(dtype != "default"):
		lst=query.split(dtype+"(")
		tquery=lst[0]+"anon_"+dtype+"("+lst[1]
		return tquery
	return query

#Function which returns transformed UnBounded Query
def fastbounded(query,dtype):
	if(dtype != "default"):
		lst=query.split(dtype+"(")
		if dtype=="count":
			return lst[0]+"anon_"+dtype+"("+lst[1]
			 
		minquery=lst[0]+"min("+lst[1]
		maxquery=lst[0]+"max("+lst[1]
		lst2=lst[1].split(')')
		tquery=lst[0]+"anon_"+dtype+"_with_bounds("+lst2[0]+",("+minquery+"),("+maxquery+"))"+lst2[1]
		return tquery
	return query
