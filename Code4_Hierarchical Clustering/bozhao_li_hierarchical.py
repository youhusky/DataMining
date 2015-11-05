import heapq
from math import sqrt
__author__ = 'Joshua'


def main():
	raw_data = get_data()
	raw_merge = pair(raw_data)
	merge_heap(raw_merge)


def get_data():
	"""

	:rtype: object
	"""
	with open('iris.dat') as filename:
		opendata = filename.readlines()
		read_data = []
		for eachline in opendata:
			read_data.append(eachline.strip().split(','))
	return read_data


def pair(data):
	merge = []
	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			merge.append([euclidean_distance(data[i][:4], data[j][:4]),(i, j)])
	return merge


def merge_heap(data):
	heap_list = []
	for i in data:
		heapq.heappush(heap_list, i)
	while 1:
		print heapq.heappop(heap_list)



def euclidean_distance(vector1, vector2):
	tsum = sum([pow((float(vector1[i]) - float(vector2[i])), 2) for i in range(len(vector1))])
	ssum = sqrt(tsum)
	return ssum

if __name__ == '__main__':
	main()
	a=[9]
	b=[10]
	print list(set(a+b))

