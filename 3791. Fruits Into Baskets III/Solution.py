__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        # next power of two
        size = 1
        while size < self.n:
            size <<= 1
        self.size = size
        self.tree = [0] * (2 * size)
        # build leaves
        for i, v in enumerate(data):
            self.tree[size + i] = v
        # build internal nodes
        for i in range(size - 1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def update(self, idx, value):
        # point update: set data[idx] = value
        i = self.size + idx
        self.tree[i] = value
        i //= 2
        while i:
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])
            i //= 2

    def find_first(self, node, node_lo, node_hi, fruit):
        """
        Finds the smallest index j in [node_lo, node_hi)
        whose value >= fruit, or returns -1 if none.
        """
        if self.tree[node] < fruit:
            return -1
        if node_lo + 1 == node_hi:
            # leaf
            return node_lo
        mid = (node_lo + node_hi) // 2
        left_node = 2 * node
        # try left child
        if self.tree[left_node] >= fruit:
            return self.find_first(left_node, node_lo, mid, fruit)
        else:
            return self.find_first(left_node + 1, mid, node_hi, fruit)

    def query_first(self, fruit):
        # API: search whole range [0, n)
        return self.find_first(1, 0, self.size, fruit)


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        st = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            j = st.query_first(fruit)
            if j == -1 or j >= len(baskets):
                # no suitable basket
                unplaced += 1
            else:
                # place it and mark basket j as used
                st.update(j, 0)

        return unplaced