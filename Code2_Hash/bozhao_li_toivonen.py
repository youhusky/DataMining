import sys
import random
from itertools import combinations

__author__ = 'Joshua'


def opendata(data):
	transform_data = []
	input_data = data.readlines()
	for data_line in input_data:
		transform_data.append(data_line.strip().split(','))
	return transform_data


def select(data):
	return random.sample(data, int(len(data)*0.4))


def count_items_1(data, support):
	frequent_items_list = {}
	for each_line in data:
		for each_items in each_line:
			frequent_items_list[each_items] = frequent_items_list.get(each_items, 0) + 1
	all_items = list(frequent_items_list)
	for each in frequent_items_list.keys():
		if frequent_items_list[each] < support:
			del (frequent_items_list[each])
	frequent_items = sorted(list(frequent_items_list))
	output_items = []
	for i in range(len(frequent_items)):
		output_items.append([frequent_items[i]])
	return frequent_items, all_items, output_items


def count_items_2(data, alldata, num):
	candidate_pairs = list(combinations(data, num))
	all_pairs = list(combinations(alldata, num))
	return candidate_pairs, sorted(list(set(all_pairs)-set(candidate_pairs)))


def frequent_items_2(data, select, length, support):
	temp_list = []
	for each in data:
		num = 0
		for items in range(len(select)):
			if set(each).issubset(set(select[items])):
				num += 1
		temp_list.append([each, num])  # temp_list = ((a,b),8)
	frequent_pairs = []
	not_frequent_pairs = []
	for each in range(len(temp_list)):
		if temp_list[each][1] >= 0.45*support:
			frequent_pairs.append(list(temp_list[each][0]))
		else:
			not_frequent_pairs.append(temp_list[each][0])
	return tuple(not_frequent_pairs), temp_list


def find_allset(candidate, raw_data, support):
	temp_list = []
	for each in candidate:
		num = 0
		for items in range(len(raw_data)):
			if set(each).issubset(set(raw_data[items])):
				num += 1
		temp_list.append((each, num))  # temp_list = ((a,b),8)
	frequent_pairs = []
	for each in range(len(temp_list)):
		if temp_list[each][1] > support:
			frequent_pairs.append(tuple(temp_list[each][0]))
	return frequent_pairs


if __name__ == '__main__':
	inputdata = open(sys.argv[1])
	support = int(sys.argv[2])
	raw_data = opendata(inputdata)
	items = 1
	while 1:
		select_data = select(raw_data)
		frequent_items_list, all_items, output1 = count_items_1(raw_data, support)  # support
		candidate_items, not_frequent_pairs = count_items_2(frequent_items_list, all_items, 2)
		not_candidate_items_pairs,all_pairs11 = frequent_items_2(candidate_items, select_data, len(raw_data), support)
		true_freq = find_allset(candidate_items, raw_data, support)
		for i in range(len(all_pairs11)):
			all_pairs11[i] = all_pairs11[i][0]
		if (len(all_pairs11)-len(true_freq)) != len(not_candidate_items_pairs):
			items += 1
		else:
			print items, '\n', '0.4'
			output = []
			for each in range(len(true_freq)):
				output.append(list(true_freq[each]))
			print output1, '\n\n', output, len(output)
			break
