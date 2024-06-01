def lastname():
	last_name = input().split('-')
	capital = ''.join(i[0] for i in last_name)
	print (capital)
	
lastname()