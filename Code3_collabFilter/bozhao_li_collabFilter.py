import sys
from math import pow, sqrt
__author__ = 'Joshua'


def main():
	User_id = sys.argv[2]
	Movie = sys.argv[3]
	K = sys.argv[4]
	neighbor = K_nearest_neighbors(User_id, K)
	Predict(User_id, Movie, neighbor)


def pearson_correlation(user1, user2):
	def avg(user):
		all = 0
		for each in user:
			all += float(each[0])
		return all/len(user)

	def denomiator(count, user):
		num = 0
		for each in count:
			num += pow((each - avg(user)), 2)
		return sqrt(num)
	usr1 = []
	usr2 = []
	for line in readdata:
		if line[0] == user1:
			usr1.append(line[1:3])
		elif line[0] == user2:
			usr2.append(line[1:3])
	count1 = []
	count2 = []
	for lines in usr1:
		for each in usr2:
			if each[1] == lines[1]:
				count1.append(float(lines[0]))
				count2.append(float(each[0]))
	number = 0
	for item in range(len(count1)):
		number += (count1[item] - avg(usr1)) * (count2[item] - avg(usr2))
	try:
		return number / (denomiator(count1, usr1) * denomiator(count2, usr2))
	except:
		return 0


def K_nearest_neighbors(user1, k):
	k = int(k)
	user_id = []
	for line in readdata:
		if line[0] != user1:
			user_id.append(line[0])
	if len(readdata) == len(user_id):
		print 'Wrong User_id!'
		return 0
	user_id = tuple(set(user_id))
	all_neighbor = {}
	for item in user_id:
		all_neighbor[item] = all_neighbor.get(item, pearson_correlation(user1, item))
	sort_neighbor = sorted(all_neighbor.iteritems(), key=lambda d: d[1], reverse=True)
	for i in sort_neighbor[:k]:
		print i[0], i[1]
	return sort_neighbor[:k]


def Predict(user1, item, k_nearest_neighbors):
	if k_nearest_neighbors == 0:
		return 0
	klist = [k[0] for k in k_nearest_neighbors]
	predict_items = []
	for line in readdata:
		if line[0] in klist and line[2] == item:
			predict_items.append([line[0], line[1]])
		if line[0] == user1 and line[2] == item:
			print '\n\n', 'You don''t need to predict this value', line[1]
			return 0
	num = 0.0
	it = 0.0
	for i in predict_items:
		num += float(i[1]) * pearson_correlation(user1, i[0])
		it += pearson_correlation(user1, i[0])
	if it == 0:
		print '\n\n', 'Wrong Movie!'
	else:
		print '\n\n', num / it

if __name__ == '__main__':
	opendata = open(sys.argv[1]).readlines()
	readdata = []
	for each in opendata:
		readdata.append(each.strip().split('\t'))
	main()



