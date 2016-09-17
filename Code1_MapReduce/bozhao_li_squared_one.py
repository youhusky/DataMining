import MapReduce
import sys

__author__ = 'Joshua'

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
size = 5


def mapper(record):
	row = record[0]
	column = record[1]
	value = record[2]
	for i in range(0, size):
		mr.emit_intermediate((row, i), (column, value))
	for j in range(0, size):
		mr.emit_intermediate((j, column), (row, value))


def reducer(key, list_of_values):
	temp_list = [location[0] for location in list_of_values]
	index_list = []
	output = 0

	# print temp_list
	for index_location in range(len(temp_list)):
		if temp_list.count(temp_list[index_location]) > 1:
			index_list.append(index_location)

	# print index_list

	for items in index_list:
		m = temp_list.index(temp_list[items])
		n = temp_list.index(temp_list[items], m + 1)
		output += list_of_values[m][1] * list_of_values[n][1]

	output /= 2
	mr.emit((key, output))


if __name__ == '__main__':
	# input_data = open(sys.argv[1])  # name

	input_data = open('matrix.json')

	mr.execute(input_data, mapper, reducer)
