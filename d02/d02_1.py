


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
		data = list(map(int,f.read().strip().split(',')))
	
	data[1] = 12
	data[2] = 2

	idx = 0
	while data[idx] != 99:
		if data[idx] in (1, 2):
			idx = functions[str(data[idx])](data, idx)
		else:
			idx = idx + 1
	print(data[0])
		
	
	

