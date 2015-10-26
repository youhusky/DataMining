import sys
from itertools import combinations
__author__ = 'Joshua'


def opendata(data):
	transfordata = []
	input_data = data.readlines()
	for data_line in input_data:
		tmp = data_line.strip().split(',')
		transfordata.append(tmp)
	return transfordata           #[['d', 'e', 'a'], ['d', 'b', 'e', 'f']]


def count_items(data, support):
	frequent_items = {}
	for each_line in data:
		for each_items in each_line:
			frequent_items[each_items] = frequent_items.get(each_items, 0) + 1
	for each in frequent_items.keys():
		if frequent_items[each] < support:
			del (frequent_items[each])
	sorted_items = sorted(list(frequent_items))
	print sorted_items, '\n'
	return sorted_items     #['a', 'b', 'c', 'd', 'e', 'f', 'g']


def find_pairs(data, num):
	candidate_raw_pairs = list(combinations(data, num))
	return candidate_raw_pairs    #[('a', 'b'), ('a', 'c')]


def count_more_pairs(data, raw_data, num):
	candidate_raw_morepairs = list(combinations(data, num))
	candidate_items_3 = []
	for i in range(len(candidate_raw_morepairs)):
		count = 0
		for j in range(len(raw_data)):
			if set(candidate_raw_morepairs[i]).issuperset(set(raw_data[j])):
				count += 1
		if count > (num-1):
			candidate_items_3.append(sorted(candidate_raw_morepairs[i]))
	return candidate_items_3


def hash_function(data, raw_data, buckets, support):
	temp_list = []
	for each in data:
		num = 0
		for items in range(len(raw_data)):
			if set(each).issubset(set(raw_data[items])):
				num += 1
		temp_list.append([each, num]) ##('a', 'b'), 8
	pairsoutput = []
	for i in range(len(temp_list)):
		if temp_list[i][1] >= support:
			pairsoutput.append(temp_list[i][0])

	output = []
	pairs_tmv = []
	for each in range(len(temp_list)):
		output.append([temp_list.index(temp_list[each]) % buckets, temp_list[each][1]])
		pairs_tmv.append([temp_list.index(temp_list[each]) % buckets, temp_list[each][0]]) #[0, ('a', 'b')
	for j in range(len(output)):
		for k in range(j + 1, len(output)-1):
			if output[j][0] == output[k][0]:
				output[k][1] = output[j][1] + output[k][1]
				del(output[j])
	dict_output = dict(output)
	output1 = []
	for each in range(len(output)):
		if output[each][1] >= support:
			bitmap = 1
			output1.append((output[each][0], bitmap))     # bitmap output
	pairs_output = []
	for each in dict(output1):
		for i in range(len(pairs_tmv)):
			if pairs_tmv[i][0] == each:
				pairs_output.append(list(pairs_tmv[i][1]))
	if len(pairsoutput) == 0:
		return pairs_output, dict_output
	else:
		print dict_output, '\n', sorted(pairsoutput), '\n'
		return pairs_output, dict_output

if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	support = int(sys.argv[2])
	buckets = int(sys.argv[3])
	raw_data = opendata(inputdata)
	sorted_items = count_items(raw_data, support)
	candidate_raw_pairs = find_pairs(sorted_items, 2)
	for num in range(3,len(sorted_items)):
		candidate_pairs, bitmap = hash_function(candidate_raw_pairs, raw_data, buckets, support)
		if len(candidate_pairs) == 0:
			break
		else:
			candidate_raw_pairs = count_more_pairs(sorted_items, candidate_raw_pairs, num)




