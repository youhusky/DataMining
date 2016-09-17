import MapReduce
import sys

__author__ = 'Joshua'

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
size = 5


def mapper(record):
	mr.emit_intermediate(tuple(record[0:2]), record[2])


def reducer(key, list_of_values):
	total = 0
	for v in list_of_values:
		total += v
	mr.emit((key, total))


if __name__ == '__main__':
	# input_data = open(sys.argv[1])  # name

	input_data = open('matrix.json')

	mr.execute(input_data, mapper, reducer)
