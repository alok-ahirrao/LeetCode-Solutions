from bisect import bisect


def tree_size(node, parent, tree, is_removed):
    size = 1
    for child in tree[node]:
        if child == parent or is_removed[child]:
            continue
        size += tree_size(child, node, tree, is_removed)
    return size


def dfs_centroid(node, parent, tree, is_removed, tree_size):
    if is_removed[node]:
        return 0, None
    node_count = 1
    is_centroid = True
    centroid_node = None
    for child in tree[node]:
        if child == parent:
            continue
        child_count, child_centroid = dfs_centroid(child, node, tree, is_removed, tree_size)
        if child_count > tree_size // 2:
            is_centroid = False
        if child_centroid is not None:
            centroid_node = child_centroid
        node_count += child_count
    if node_count < tree_size // 2:
        is_centroid = False
    return node_count, (node if is_centroid else centroid_node)


def calculate(node, tree, is_removed, values, k):
    global_list = [(0, node)]
    for child in tree[node]:
        if is_removed[child]:
            continue
        stack = [(1, child, node)]
        child_list = []
        while stack:
            distance, current_node, parent_node = stack.pop()
            child_list.append((distance, current_node))
            for child_node in tree[current_node]:
                if is_removed[child_node] or child_node == parent_node:
                    continue
                stack.append((distance + 1, child_node, current_node))
        child_list.sort()
        for distance, current_node in child_list:
            values[current_node] -= bisect(child_list, k - distance, key=lambda value: value[0])
        global_list.extend(child_list)
    global_list.sort()
    for distance, current_node in global_list:
        values[current_node] += bisect(global_list, k - distance, key=lambda value: value[0])


def solve(node, tree, is_removed, values, k):
    size = tree_size(node, -1, tree, is_removed)
    centroid = dfs_centroid(node, -1, tree, is_removed, size)[1]
    is_removed[centroid] = True
    calculate(centroid, tree, is_removed, values, k)
    for child in tree[centroid]:
        if not is_removed[child]:
            solve(child, tree, is_removed, values, k)


def build_and_solve(edges, k):
    tree = [[] for _ in range(len(edges) + 1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    is_removed = [False] * len(tree)
    values = [0] * len(tree)
    solve(0, tree, is_removed, values, k)
    return values

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        values = build_and_solve(edges1, k)
        if not k:
            return values
        max_value = max(build_and_solve(edges2, k - 1))
        return [value + max_value for value in values]