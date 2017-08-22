#!/usr/bin/env python
#广度优先搜索
from collections import deque
graph = {}
graph['you'] = ["alice",'Bob','claire']
graph['Bob'] = ['anuj', 'peggy']
graph["alice"] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['thom'] = []
graph['jonny'] = []
graph['peggy'] = []


def find_seller():
	search_queue = deque()

	search_queue += graph['you']

	while search_queue:
		person = search_queue.popleft()
		if person_is_seller(person):
			print person + "is doo!"
			return True
		else:
			search_queue += graph[person]

	return False

def person_is_seller(name):
	return name[-1] == 'm'

print find_seller()
