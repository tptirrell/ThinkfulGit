import sqlite3 as lite
import pandas as pd

con = lite.connect("cityweather.db")

with con:
	cur = con.cursor()    
	cur.execute("drop table if exists cities")
	cur.execute("drop table if exists weather")
	cur.execute("create table cities (name text, state text)")
	cur.execute("create table weather (city text, year integer, highmonth text, lowmonth text, avghigh integer)")   
	cur.execute("insert into cities (name,state) values ('New York City', 'NY'),('Boston', 'MA'),('Chicago', 'IL'),('Miami', 'FL'),('Dallas', 'TX'),('Seattle', 'WA'),('Portland', 'OR'),('San Francisco', 'CA'),('Los Angeles', 'CA');")
	cur.execute("insert into weather (city,year,highmonth,lowmonth,avghigh) values ('New York City',2013,'July','January',62),('Boston',2013,'July','January',59),('Chicago',2013,'July','January',59),('Miami',2013,'August','January',84),('Dallas',2013,'July','January',77),('Seattle',2013,'July','January',61),('Portland',2013,'July','December',63),('San Francisco',2013,'September','December',64),('Los Angeles',2013,'September','December',75);")

	cur.execute("select name,state,highmonth,avghigh from cities inner join weather on name = city;")
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)
	
	julycities = df[df['highmonth']=='July']
	citystatejuly = [julycities['name'] + ", " +julycities['state']]


	print ("The cities that are the warmest in July are")
	for i in range(len(citystatejuly[0])):
		try: print (citystatejuly[0][i])
		except: pass
