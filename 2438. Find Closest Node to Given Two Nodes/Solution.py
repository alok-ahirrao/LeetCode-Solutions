class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        visited1 = set()
        visited2 = set()
        while node1 != -1 or node2 != -1:
            if node1 in visited1:
                node1 = -1
            
            if node2 in visited2:
                node2 = -1

            if node1 != -1:
                visited1.add(node1)
            
            if node2 != -1:
                visited2.add(node2)

            if node1 in visited2 and node2 in visited1:
                return min(node1, node2)
            
            if node1 in visited2:
                return node1
            
            if node2 in visited1:
                return node2
            
            if node1 != -1:
                node1 = edges[node1]

            if node2 != -1:
                node2 = edges[node2]       
                 
        return -1