import pandas as pd

route_stop_df = pd.read_csv('route_stop.csv')
stops_df = pd.read_csv('stops.csv')

stop_names_list = stops_df['stop_name'].tolist()		#answer for part 1
#print(stop_names_list)
stop_id_set = stops_df['stop_id'].tolist()

stop_id_list = route_stop_df['stop_id'].tolist()

print(stop_id_list.count(2))
'''def create_stop_list(stop_names_list: list, n: int, stops_df: df)-> list:
	for stop_index in range(len(stop_names_list)):
		if stops_df.at[stop_index, '']'''

def get_crowded_stops(route_stop_df, stops_df, stop_id_list: list, stop_id_set: list, n: int) -> list:
	crowded_stops_list = []
	for stop_id in range(len(stop_id_set)):
		if stop_id_list.count(stop_id_set[stop_id]) <= n:
			crowded_stops_list.append(stops_df.at[stop_id, 'stop_name'])
	return crowded_stops_list

print(get_crowded_stops(route_stop_df, stops_df,stop_id_list, stop_id_set, 12))
