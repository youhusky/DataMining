import heapq

__author__ = 'Joshua'
b = []
a = [1,2,3,4,5,6,7,7,8,8,9,1,2]
for each in a:
	heapq.heappush(b, each)
sort = []
while b:
	sort.append(heapq.heappop(b))
print sort
