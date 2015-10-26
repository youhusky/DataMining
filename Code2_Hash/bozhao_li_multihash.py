import sys
from itertools import combinations
__author__ = 'Joshua'


def opendata(data):
	transfor_data = []
	input_data = data.readlines()
	for data_line in input_data:
		tmp = data_line.strip().split(',')
		transfor_data.append(tmp)
	return transfor_data


def count_items_1(data, support):
	frequent_items = {}
	for each_line in data:
		for each_items in each_line:
			frequent_items[each_items] = frequent_items.get(each_items, 0) + 1
	for each in frequent_items.keys():
		if frequent_items[each] < support:
			del (frequent_items[each])
	sorted_items = sorted(list(frequent_items))
	print sorted_items
	return sorted_items


def find_pairs(data, num):
	candidate_items = list(combinations(data, num))
	return candidate_items


def count_morepairs(data, raw_data, num):
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


def frequent_items_2(data, raw_data, num_buckets, support):
	def hash_table1(temp, num_buckets):
		output = []
		pairs_tmv = []
		for each in range(len(temp_list)):
			output.append([temp_list.index(temp_list[each]) % num_buckets, temp_list[each][1]])
			pairs_tmv.append([temp_list.index(temp_list[each]) % num_buckets, temp_list[each][0]])
		for j in range(len(output)):
			for k in range(j + 1, len(output)):
				if output[j][0] == output[k][0]:
					output[k][1] = output[j][1] + output[k][1]
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
		bitmap_dict = dict(output1)
		temp_dict = {}
		bucket_number = []
		for k in range(int(num_buckets)):
			bucket_number.append(k)
		temp_dict = temp_dict.fromkeys(bucket_number, 0)
		temp_dict.update(dict(output))
		return temp_dict, bitmap_dict

	def hash_table2(temp, num_buckets):
		output = []
		pairs_tmv = []
		for each in range(len(temp_list)):
			output.append([7 * (temp_list.index(temp_list[each]) / 3) % num_buckets, temp_list[each][1]])
			pairs_tmv.append([7 * (temp_list.index(temp_list[each]) / 3) % num_buckets, temp_list[each][0]])
		for j in range(len(output)):
			for k in range(j + 1, len(output)):
				if output[j][0] == output[k][0]:
					output[k][1] = output[j][1] + output[k][1]
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
		bitmap_dict = dict(output1)
		temp_dict = {}
		bucket_number = []
		for k in range(int(num_buckets)):
			bucket_number.append(k)
		temp_dict = temp_dict.fromkeys(bucket_number, 0)
		temp_dict.update(dict(output))
		return temp_dict, bitmap_dict

	temp_list = []
	for each in data:
		count = 0
		for items in range(len(raw_data)):
			if set(each).issubset(set(raw_data[items])):
				count += 1
		temp_list.append((each, count))  # temp_list = ((a,b),8)
	frequent_pairs = []
	for each in range(len(temp_list)):
		if temp_list[each][1] >= support:
			frequent_pairs.append(list(temp_list[each][0]))
	if len(frequent_pairs) == 0:
		return frequent_pairs
	else:
		output_dict_1, bitmap_1 = hash_table1(temp_list, num_buckets)
		output_dict_2, bitmap_2 = hash_table2(temp_list, num_buckets)
		print '\n', output_dict_1, '\n',output_dict_2, '\n', frequent_pairs
		return frequent_pairs


if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	support = int(sys.argv[2])
	buckets = int(sys.argv[3])
	raw_data = opendata(inputdata)
	frequent_items = count_items_1(raw_data, support)  #
	candidate_items = find_pairs(frequent_items, 2)  ## items 2
	for num in range(3, len(frequent_items)):
		output = frequent_items_2(candidate_items, raw_data, buckets, support)
		if len(output) == 0:
			break
		else:
			candidate_items = count_morepairs(frequent_items, output, num)

