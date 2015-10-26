import MapReduce
import sys
__author__ = 'Joshua'

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


def mapper(record):
    # key: hashable 2-item sets
    # value:  count
    if len(record) > 1:  # find 2-item sets
        for i in range(len(record)):
            for j in range(i + 1, len(record)):
                items = []
                items.append(record[i])
                items.append(record[j])
                mr.emit_intermediate(tuple(sorted(items)), 1)
    else:
        pass


def reducer(key, list_of_values):
    # key: 2-item sets
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        total += v
    if total > 100:
        mr.emit(key)

if __name__ == '__main__':
    inputdata = open(sys.argv[1])  # name
    mr.execute(inputdata, mapper, reducer)
