import heapq
from math import sqrt
from itertools import combinations
import sys

__author__ = 'Joshua'

'''
add dimension = len(raw_data[0])-1
in order to solve the problem that each of n dimensions

'''
def main():
	file_name = sys.argv[1]
	number = sys.argv[2]

	raw_data = get_data(file_name)
	dimension = len(raw_data[0])-1
	standard_value = standard_class(raw_data, dimension)
	raw_merge, value = pair(raw_data, dimension)
	result = get_items_distance(raw_merge, value, int(number))
	evaluate(result, standard_value)
	for each_calss in result:
		print each_calss


def get_data(name):
	"""

	:rtype: object
	"""
	with open(name) as filename:
		opendata = filename.readlines()
		read_data = [eachline.strip().split(',') for eachline in opendata]

	return read_data


def standard_class(raw_data, dimension):
	var = [raw_data[classname][dimension] for classname in range(len(raw_data))]
	var = list(set(var))
	object_standard_class = []
	for each_classname in range(len(var)):
		temp = []
		for object_index in range(len(raw_data)):
			if raw_data[object_index][dimension] == var[each_classname]:
				temp.append(object_index)
		object_standard_class.append(temp)
	return object_standard_class


def pair(data,dimension):
	"""

	:rtype: object
	"""
	merged_distance = []
	object_value = []

	for object_index_i in range(len(data)):
		object_value.append([object_index_i, data[object_index_i][:dimension]])
		for object_index_j in range(object_index_i + 1, len(data)):
			merged_distance.append([euclidean_distance(data[object_index_i][:dimension],
			                                 data[object_index_j][:dimension]),
			                              [object_index_i, object_index_j]])
	return merged_distance, object_value


def euclidean_distance(vector1, vector2):
	return sqrt(sum([pow((float(vector1[i]) - float(vector2[i])), 2) for i in range(len(vector1))]))


def get_items_distance(raw_data, raw_value, number):
	def get_centroid(part1, part2, item_list):
		final_join_object = []
		if type(part1) == int and type(part2) == int:
			for each_object in range(len(item_list[part1])):
				final_join_object.append((float(item_list[part1][each_object])
				                    + float(item_list[part2][each_object])) / 2.0)
			return final_join_object
		elif type(part1) == int and type(part2) != int:
			for each_object in part2:
				final_join_object.append(each_object)
			final_join_object.append(part1)
			final_value = []
			for each_object in range(len(item_list[each_object])):
				temp = []
				for dimension in range(len(final_join_object)):
					temp.append(float(item_list[final_join_object[dimension]][each_object]))
				final_value.append(sum(temp) / len(final_join_object))
			return final_value
		elif type(part1) != int and type(part2) == int:
			for each_object in part1:
				final_join_object.append(each_object)
			final_join_object.append(part2)
			final_value = []
			for each_object in range(len(item_list[each_object])):
				temp = []
				for dimension in range(len(final_join_object)):
					temp.append(float(item_list[final_join_object[dimension]][each_object]))
				final_value.append(sum(temp) / len(final_join_object))
			return final_value
		else:
			for each_object in part1:
				final_join_object.append(each_object)
			for dimension in part2:
				final_join_object.append(dimension)
			final_value = []
			for each_object in range(len(item_list[each_object])):
				temp = []
				for dimension in range(len(final_join_object)):
					temp.append(float(item_list[final_join_object[dimension]][each_object]))
				final_value.append((sum(temp) / len(final_join_object)))
			return final_value
	if number == 1:
		return [[raw_value.index(i) for i in raw_value]]
	data = raw_data
	item_list = [object[1] for object in raw_value]
	merge_dict = {}
	for object in raw_value:
		merge_dict[object[0]] = object[1]  # dict save (2,3):[1.1,2.2,3.3,4.4]
	'''
	'''

	heap_list = []
	for each_heap in data:
		heapq.heappush(heap_list, each_heap)
	distance, merged_items = heapq.heappop(heap_list)

	while len(merge_dict) > number:

		'''
		tuple union: three part int + (), ()+int and ()()
		'''
		if type(merged_items[0]) == tuple and type(merged_items[1]) == tuple:
			merge_dict[tuple(sorted(set(merged_items[0]).union(set(merged_items[1]))))] = \
				get_centroid(merged_items[0], merged_items[1], item_list)

		elif type(merged_items[0]) == tuple or type(merged_items[1]) == tuple:
			if type(merged_items[0]) == tuple and type(merged_items[1]) != tuple:
				temp = [merged_items[1]]
				for num in merged_items[0]:
					temp.append(num)
				merge_dict[tuple(temp)] = \
					get_centroid(merged_items[0], merged_items[1], item_list)

			elif type(merged_items[1]) == tuple and type(merged_items[0]) != tuple:
				temp = [merged_items[0]]
				for num in merged_items[1]:
					temp.append(num)
				merge_dict[tuple(temp)] = \
					get_centroid(merged_items[0], merged_items[1], item_list)
		else:
			merge_dict[tuple(sorted(merged_items))] = \
				get_centroid(merged_items[0], merged_items[1], item_list)

		merge_dict.pop(merged_items[0])
		merge_dict.pop(merged_items[1])

		heap_list = []
		for object in merge_dict:
			for j in merge_dict:
				if object != j:
					heap_list.append([euclidean_distance(merge_dict[object], merge_dict[j]), [object, j]])
		tep = []
		for each_heap in heap_list:
			heapq.heappush(tep, each_heap)
		distance, merged_items = heapq.heappop(tep)
	temp = []
	for object in merge_dict:
		if type(object) == int:
			temp.append([object])
		else:
			temp.append(sorted(list(object)))
	return temp
	#return [sorted(list(object)) for object in merge_dict]


def evaluate(result, standard_value):
	def get_list(value):
		temp = [list(combinations(i, 2)) for i in value]
		return [each_classvalue for each_class in range(len(temp)) for each_classvalue in temp[each_class]]
	test = get_list(result)
	standard = get_list(standard_value)
	tp = set(standard).intersection(set(test))
	precision = float(len(tp)) / float(len(test))
	recall = float(len(tp)) / float(len(standard))
	print precision, '\n', recall


if __name__ == '__main__':
	main()
