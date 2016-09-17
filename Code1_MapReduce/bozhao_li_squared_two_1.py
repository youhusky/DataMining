import MapReduce
import sys
import re

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
	mr.emit_intermediate(column, ('A', row, value))
	mr.emit_intermediate(row, ('B', column, value))


def reducer(key, list_of_values):
	a_matrix = []
	b_matrix = []
	for num in range(len(list_of_values)):
		if list_of_values[num][0] == 'A':
			a_matrix.append(list_of_values[num])
		else:
			b_matrix.append(list_of_values[num])

	for i in range(len(a_matrix)):
		for j in range(len(b_matrix)):
			mr.emit(
				((a_matrix[i][1], b_matrix[j][1]), a_matrix[i][2] * b_matrix[j][2]))


if __name__ == '__main__':
	# input_data = open(sys.argv[1])  # name

	input_data = open('matrix.json')

	mr.execute(input_data, mapper, reducer)
