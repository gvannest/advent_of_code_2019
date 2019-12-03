


def ft_1(data, idx):
	data[data[idx + 3]] = data[data[idx + 1]] + data[data[idx + 2]]
	return idx + 4


def ft_2(data, idx):
	data[data[idx + 3]] = data[data[idx + 1]] * data[data[idx + 2]]
	return idx + 4


if __name__ == "__main__":
	
	functions = {
		"1": ft_1,
		"2": ft_2,
		}

	with open('./data.txt', 'r') as f:
		data_init = list(map(int,f.read().strip().split(',')))
	
	data_init[1] = 12
	data_init[2] = 2

	for i in range(100):
		for j in range(100):
			data = data_init[:]
			data[1] = i
			data[2] = j
			idx = 0
			while data[idx] != 99:
				if data[idx] in (1, 2):
					idx = functions[str(data[idx])](data, idx)
				else:
					idx = idx + 1
			if data[0] == 19690720:
				print("noun : {}".format(data[1]))
				print("verb : {}".format(data[2]))
				print("answer : {}".format(100*data[1] + data[2]))
				exit()
		
	
	

