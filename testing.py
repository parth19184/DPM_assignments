import pandas
import pickle
'''agency_file = open('csvfiles/agency.csv')
print(agency_file.read(17))'''

'''cars = ['merc', 'bmw', 'tata']
file_name = "mycar.pkl"
fileobj = open(file_name, "wb")
pickle.dump(cars, fileobj)
fileobj.close()'''

file_name = "mycar.pkl"
file_obj = open(file_name, 'rb')
mycar = pickle.load(file_obj)
print(mycar)
print(type(mycar))
file_obj.close()