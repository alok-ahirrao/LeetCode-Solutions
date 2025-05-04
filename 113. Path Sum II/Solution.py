# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.node_parent = { None: None, root: None }
        self.valid_path_sum_leaf_nodes = []

        def find_node_parents(node):
            """
            Find the node parent for each node in the tree.
            """
            if not node:
                return
            
            if node.left:
                self.node_parent[node.left] = node
                find_node_parents(node.left)
            
            if node.right:
                self.node_parent[node.right] = node
                find_node_parents(node.right)
            
        def find_path_sum(node, target_sum):
            """
            Find all the leaf nodes that have a path sum equal to target sum.
            """
            if not node:
                return
            
            target_sum -= node.val

            if not node.left and not node.right:
                if target_sum == 0:
                    self.valid_path_sum_leaf_nodes.append(node)

                return

            find_path_sum(node.left, target_sum)
            find_path_sum(node.right, target_sum)
        
        def construct_node_to_root_path(node):
            """
            Construct a path array of the node vals from the root to the current node.
            """
            path_arr = []

            while node:
                path_arr.append(node.val)
                node = self.node_parent[node]
            
            path_arr.reverse()
            return path_arr
        
        find_node_parents(root)
        find_path_sum(root, targetSum)

        # For each valid path sum leaf node, transform them into a valid path array of vals from the root to the current node.
        valid_path_sum_paths = [construct_node_to_root_path(leaf_node) for leaf_node in self.valid_path_sum_leaf_nodes]

        return valid_path_sum_paths