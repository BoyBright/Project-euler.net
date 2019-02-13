from collections import deque

graph = dict()
graph['ada'] = ['earn', 'nut', 'jate']
graph['earn'] = ['ben', 'meen', 'bright']
graph['nut'] = ['jame', 'tim', 'bright']
graph['jate'] = ['bright']

is_seller = lambda name: name[-1] == 'm'

search_list = deque()
search_list += graph['ada']
searched = []

while search_list:
    candidate = search_list.popleft()
    if candidate not in searched:
        if is_seller(candidate):
            print(candidate, 'is a lotto seller')
            break
        else:     
            search_list += graph.get(candidate, [])
            searched.append(candidate)