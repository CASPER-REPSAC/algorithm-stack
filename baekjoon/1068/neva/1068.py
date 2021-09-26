from sys import stdin

N = int(stdin.readline())
nodes_parent_idxs = [*map(int, stdin.readline().strip().split(' '))]
remove_node_idx = int(stdin.readline())

root_node_i = None
graph = [{'childs': []} for _ in range(N)]

for node_i, parent_i in enumerate(nodes_parent_idxs):
  if not root_node_i and parent_i == -1:
    root_node_i = node_i
  else:
    graph[parent_i]['childs'].append(node_i)

def get_num_of_leaf_and_remove_node_using_dfs(node):
  cnt = 0
  for child_node_i in node['childs']:
    if child_node_i != remove_node_idx:
      cnt += get_num_of_leaf_and_remove_node_using_dfs(graph[child_node_i])
  if not node['childs'] or \
    len(node['childs']) == 1 and node['childs'][0] == remove_node_idx:
    cnt += 1 
  return cnt  

cnt_leaf = 0 if root_node_i == remove_node_idx \
              else get_num_of_leaf_and_remove_node_using_dfs(graph[root_node_i])
print(cnt_leaf)

# f = (lambda node_i: node_i - remove_node_idx and 
#                     (sum(f(i) for i, parent_i in enumerate(nodes_parent_idxs) if parent_i == node_i) or 1))
# print(f(nodes_parent_idxs.index(-1)))
