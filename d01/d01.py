import math

def fuel_calc(x):
	fuel = math.floor(x / 3) - 2
	if fuel < 0:
		return 0
	return fuel + fuel_calc(fuel)
	

if __name__ == "__main__":

	path = './data.txt'

	file = open(path, 'r')

	data_list = file.readlines()
	data_list = [int(x.replace('\n', '')) for x in data_list]
	print(fuel_calc(1969))	
	print(sum([fuel_calc(x) for x in data_list]))
	
	
