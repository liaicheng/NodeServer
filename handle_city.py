from pymongo import MongoClient

db_url = 'localhost:27017'
conn = MongoClient('mongodb://%s/' %db_url)
collections = [conn['geo']['new_city'],conn['geodb']['new_city_county'],
	conn['geodb']['new_county_state'],conn['irctoryperdb']['statecities']]

def handle():
	db_url = 'localhost:27017'
	conn = MongoClient('mongodb://%s/' %db_url)
	states = conn['geo']['new_county_state'].distinct('state')
	print states.count
	for state in states:
		county = []
		
		counties = conn['geo']['new_county_state'].find({"state":state})
		i = 0
		for c in counties:
			
			cou = c['county_name']
			cou_key = c['new_county_key']

			cities = conn['geo']['new_city_county'].find({"county_key":cou_key})
			city = {}
			
			j = 0
			for ci in cities:
				city_key = ci['city_key']
				city_names = conn['geo']['new_city'].find({'new_city_key':city_key})

				city_name = ''
				old_city_key =''
				nbhs=[]
				for cn in city_names:
					city_name = cn['city_name']
					old_city_key = cn['city_key']
					# print old_city_key
					# print city_name
				if old_city_key <> '':
					nbs = conn['geo']['neighborhood_city'].find({'igen_city_code':old_city_key})
					for nb in nbs:
						an_geo_area = nb['an_geo_area']
						arears = conn['geo']['neighborhood'].find({'an_geo_area':an_geo_area})
						for area in arears:
							nbhs.append(area['geo_area_name'])
						print nbhs

				city[city_name]=nbhs
				j=j+1

			doc ={"state":state,"county":cou,"city":city}
			#print doc
			#quit()
			if nbhs <>[]:
				print nbhs
				quit()
				conn['irctoryperdb']['statecities'].insert(doc)
			




if __name__== "__main__":
	handle()