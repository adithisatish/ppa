
#Function to idetify type
def find(query):
	q = query.lower()
	lst=q.split("from")[0]
	types=["count","sum","avg","var","stdev"]	
	for i in types:
		if (i+"(") in lst:
			return i
	return "default"

#Function which returns transformed Bounded Query
def bounded(query,dtype):
	if(dtype != "default"):
		if dtype in query:
			lst=query.split(dtype+"(")
		else:
			lst = query.split(dtype.upper()+"(")
		tquery=lst[0]+"anon_"+dtype+"("+lst[1]
		return tquery
	return query

#Function which returns transformed UnBounded Query
def fastbounded(query,dtype):
	if(dtype != "default"):
		if dtype in query:
			lst=query.split(dtype+"(")
		else:
			lst = query.split(dtype.upper()+"(")
		if dtype=="count":
			return lst[0]+"anon_"+dtype+"("+lst[1]
			 
		minquery=lst[0]+"min("+lst[1]
		maxquery=lst[0]+"max("+lst[1]
		lst2=lst[1].split(')')
		tquery=lst[0]+"anon_"+dtype+"_with_bounds("+lst2[0]+",("+minquery+"),("+maxquery+"))"+lst2[1]
		return tquery
	return query


#Function which returns intrinsically private query with winsorized bounds
def winsorized(query,dtype):
	if(dtype != "default"):
		if dtype in query:
			lst=query.split(dtype+"(")
		else:
			lst = query.split(dtype.upper()+"(")
		if dtype =="count":
			return lst[0]+"anon_"+dtype+"("+lst[1]

		att = lst[1].split(")")
		#print(att)
		temp = (att[1]).lower().split("from ",1)[1]
		table = temp
		if "(" in temp and "group by" in temp:
			table = (temp.split("("))[0].split(" group by")[0]
		elif "group by" in temp:
			table = temp.split(" group by")[0]
		#elif 
		print(table)

		lowerbound = "select percentile_cont(0.15) within group(order by " + att[0] + ") from " + table
		upperbound = "select percentile_cont(0.85) within group(order by " + att[0] + ") from " + table

		tquery = lst[0] + "anon_" + dtype + "_with_bounds(" + att[0] + ",(" + lowerbound + "),(" + upperbound + ")) from " + temp
		return tquery

	return query