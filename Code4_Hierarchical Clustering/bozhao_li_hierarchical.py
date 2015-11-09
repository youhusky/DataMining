import heapq
from math import sqrt
__author__ = 'Joshua'


def main():
	raw_data = get_data()
	raw_merge = pair(raw_data)
	merge_heap(raw_merge, raw_data)


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
	"""

	:rtype: object
	"""
	merge = []

	for i in range(len(data)):
		for j in range(i + 1, len(data)):
			merge.append([euclidean_distance(data[i][:4], data[j][:4]), [i, j]])
	return merge


def merge_heap(data, raw):
	heap_list = []
	for k in data:
		heapq.heappush(heap_list, k)
	merged_list = []
	tmv,tmq = heapq.heappop(heap_list)
	merged_list.append(tmq)
	while 1:
		distance, merged_items = heapq.heappop(heap_list)
		flag = 0
		for i in merged_list:
			tmp = [val for val in i if val in merged_items]
			if tmp == i:
				flag = 0
				break
			elif len(tmp) > 0 and tmp != i:
				flag = 1
				break
			else:
				flag = 1
		if flag == 1:
			merged_list.append(merged_items)
			add_list = []
			for j in range(len(raw)):
				if j in merged_items:
					pass
				else:
					for k in range(len(merged_items)):
						min_value = []
						min_value.append(euclidean_distance(raw[merged_items[k]][:4], raw[j][:4]))
					new_merged = merged_items[:]
					new_merged.append(j)
					add_list.append([min(min_value), new_merged])
			heap_list.extend(add_list)
			new = []
			for each in merged_list:
				if set(tuple(merged_items)).issuperset(set(tuple(each))):
					pass
				else:
					new.append(each)

			for i in range(len(merged_list)-1):
				if set(tuple(merged_items)).intersection(set(tuple(merged_list[i]))):
					#print set(tuple(merged_items)).intersection(set(tuple(merged_list[i])))

					new.remove(merged_list[i])

					merged_items = list(set(tuple(merged_items)).union(set(tuple(merged_list[i]))))

				else:
					pass
			new.append(merged_items)
			merged_list = new
			print 'a', merged_list

		else:
			pass




def euclidean_distance(vector1, vector2):

	t_sum = sum([pow((float(vector1[i]) - float(vector2[i])), 2) for i in range(len(vector1))])
	s_sum = sqrt(t_sum)
	return s_sum

if __name__ == '__main__':
	main()


