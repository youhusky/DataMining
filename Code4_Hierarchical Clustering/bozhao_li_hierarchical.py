import heapq
from math import sqrt
__author__ = 'Joshua'

def main():
	raw_data = get_data()
	print raw_data



def get_data():
	with open('iris.dat') as filename:
		opendata = filename.readlines()
		read_data = []
		for eachline in opendata:
			read_data.append(eachline.strip().split(','))
	return read_data


def euclidean_distance(vector1, vector2):
	tsum = sum([pow((vector1[i] - vector2[i]), 2) for i in range(len(vector1))])
	ssum = sqrt(tsum)
	return ssum

if __name__ == '__main__':
	main()
