import matplotlib.pyplot as plt
import sys
import networkx as nx
import community

__author__ = 'Joshua'


def main():
	new_graph = build_graph()
	value = step(new_graph)

	draw_graph(new_graph, value)


def build_graph():
	with open(sys.argv[1]) as filename:
		opendata = filename.readlines()
		readgraph = [eachline.strip().split(' ') for eachline in opendata]
		G = nx.Graph()
		G.add_edges_from(readgraph)
		return G


def step(graph):
	def own_betweenness(tempgraph):
		class NODE(object):
			def __init__(self):
				self.parent = None
				self.number = []
				self.children = []

			def bfs(self, node):
				queue = [self.parent]
				while len(queue):
					node = queue.pop(0)
					yield node
					for child in self.children:
						queue.append(child)
				return

		def path(node, betweenness):
			parent_node = {}  # if node has parent, key = node value = parent
			number_of_parentnode = {}  # the number of each node's parent
			for each_node in tempgraph:
				parent_node[each_node] = []
				if each_node == node:
					number_of_parentnode[node] = 1.0
					NODE.children = each_edge
				else:
					number_of_parentnode[each_node] = 0.0
			temp = [node]
			rootlist = []
			temp_numofparent = {node: 0}
			while temp:
				try:
					for neighbor in tempgraph[temp[0]]:
						NODE.children = neighbor
						if neighbor in temp_numofparent:
							pass
						else:
							temp_numofparent[neighbor] = temp_numofparent[temp[0]] + 1
							temp.append(neighbor)
						# NODE.bfs(neighbor)
						if temp_numofparent[neighbor] == temp_numofparent[
							temp[0]] + 1:
							number_of_fathervalue = number_of_parentnode[temp[0]]
							number_of_parentnode[neighbor] = number_of_fathervalue + number_of_parentnode[
								neighbor]
							NODE.number = number_of_parentnode[neighbor]
							parent_node[neighbor].append(temp[0])
					rootlist.append(temp[0])  # root-leaf
					del temp[0]
				except:
					pass
			para = {}
			for each_node in rootlist:
				para[each_node] = 0
			while len(rootlist) > 0:

				# len(rootlist)
				try:
					neighbor = rootlist.pop()
				except:
					pass
				for next_node in parent_node[neighbor]:  # 1+ DAG
					if (next_node, neighbor) in betweenness:
						betweenness[(next_node, neighbor)] += \
							number_of_parentnode[next_node] * \
							(1.0 + para[neighbor]) / number_of_parentnode[neighbor]
					else:
						betweenness[(neighbor, next_node)] += \
							number_of_parentnode[next_node] * \
							(1.0 + para[neighbor]) / number_of_parentnode[neighbor]
					para[next_node] += number_of_parentnode[next_node] * \
					                   (1.0 + para[neighbor]) / number_of_parentnode[neighbor]

		betweenness = {}
		for each_edge in tempgraph.edges():
			'''
			start 0.0 for all edges
			'''
			betweenness[each_edge] = 0.0
		for node in tempgraph:
			path(node, betweenness)
		for value in betweenness:
			'''
			each edge / 2
			'''
			betweenness[value] *= 0.5
		return betweenness

	temp = graph.copy()
	origin_ncomp = nx.number_connected_components(graph)
	ncomp = origin_ncomp
	temp_dict = {}
	class_dict = {}
	while ncomp < len(graph.nodes()):
		comp = own_betweenness(temp)
		max_bet = max(comp.values())
		for k, v in comp.iteritems():
			if float(v) == max_bet:
				temp.remove_edge(k[0], k[1])
		node_part = list(nx.connected_components(temp))

		child_dict = {}
		num = 0
		for each_part in node_part:
			for each_node in each_part:
				child_dict[each_node] = num
			num += 1
		class_dict[community.modularity(child_dict, graph)] = node_part
		temp_dict[community.modularity(child_dict, graph)] = child_dict
		ncomp = nx.number_connected_components(temp)

	max_modularity = max(temp_dict.keys())
	result = temp_dict[max_modularity]
	output = class_dict[max(class_dict.keys())]
	output_result(output)
	value = [result[i] for i in result]

	return value


def output_result(output):
	result = []
	for i in output:
		temp = [int(j) for j in i]
		result.append(sorted(temp))
	result = sorted(result)
	for i in result:
		print i


def draw_graph(graph, value):
	nx.draw_networkx(graph, node_color=value)
	plt.axis('off')
	# plt.show()
	plt.savefig(sys.argv[2])


if __name__ == '__main__':
	main()
