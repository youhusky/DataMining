import re
import sys
import MapReduce

__author__ = 'Joshua'

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


def mapper(record):
	# key: document contents
	# value:  document identifier
	key = record[1]
	value = record[0]
	r = re.sub(r"\W", " ", key)  # delete punctuation character
	words = r.split()
	for w in words:
		mr.emit_intermediate(w.lower(), value)  # normalize the tokens


def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts

	new_dict = {}
	unique_list = list(set(list_of_values))  # count number of documents
	for i in list_of_values:
		# count the frequency of each word on the sentence
		new_dict[i] = list_of_values.count(i)

	mr.emit((key, len(unique_list), (new_dict.items())))


if __name__ == '__main__':
	# input_data = open(sys.argv[1])

	input_data = open('books.json')  # name
	mr.execute(input_data, mapper, reducer)
