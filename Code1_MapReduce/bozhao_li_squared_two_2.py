import MapReduce
import sys
__author__ = 'Joshua'

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
size = 5


def mapper(record):
    print tuple(record[0:2])
    mr.emit_intermediate(tuple(record[0:2]), record[2])


def reducer(key, list_of_values):
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])  # name
    mr.execute(inputdata, mapper, reducer)
