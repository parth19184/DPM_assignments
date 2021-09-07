import pickle
import numpy as np
from geopy.distance import geodesic
import sys

def construct_matrix(file_name):
    with open('{}'.format(file_name)) as f:
        stops_list = f.readlines()
    final_list = list(line.replace("\n", "") for line in stops_list)
    #print(final_list[1])
    #final_list = list(line.split(",") for line in stops_list)
    
    return list((line.split(",") for line in final_list))

def get_nearest_stop(stops_matrix, input_coord):        #returns distance in m and stop_id as a tuple
    distance_list = []
    for i in stops_matrix[1:]:
        #print(geodesic((float(i[3]), float(i[4])), input_coord).m)
        #print(i[0],(float(i[3]), float(i[4])))
        distance_list.append((geodesic((float(i[3]), float(i[4])), input_coord).km, int(i[0])))
        
    return min(distance_list)

trip_route_dict = {}
penalty_stops = [5518,5526,5543,6401,7039, 7212,7271,7920,7259,8343,8349,9072,9405,9644]   #these are the stops_ids of all the stops whose naming caused a problem in the file handling, having a ","
stops_matrix = construct_matrix("csvfiles/stops.csv")    
                                  #in the middle is troublesome when only using file handling as the csv data is also not enclosed with quotes
#print(stops_matrix[1])                                                                    #the first penalty stop is missing, it was a 't-point noida' type stop
                                                                                            #all commas are replaced by "-"

'''input_coord = (28.854546,77.097907)
output_coord = (28.837182,77.098223)
input_distance = get_nearest_stop(stops_matrix, input_coord)
output_distance = get_nearest_stop(stops_matrix, output_coord)'''

#stopping condition
'''if input_distance[0] > 0.3 and output_distance[0] > 0.3:
    sys.exit("NO")
else:
    print("YES")'''
trips_matrix = np.array(construct_matrix("csvfiles/trips.csv"))
print(np.count_nonzero(trips_matrix[:,0] == '0'))