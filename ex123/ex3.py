cities = {'WH':'WuHan', 'ZJ':'ZhenJiang', 'BJ':'BeiJing'}
cities['NJ'] = 'NanJing'
cities['JX'] = 'JiangXi'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."

cities['_find'] = find_city

while True:
	print("State? (Enter to quit)")
	state = print("> ")

	if not state:  break

	city_found = cities['_find'](cities, state)
	print(city_found)