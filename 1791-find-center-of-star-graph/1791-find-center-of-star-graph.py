class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        my_list = {}
        for node1, node2 in edges:
            if node1 not in my_list:
                my_list[node1] = []
            if node2 not in my_list:
                my_list[node2] = []
            my_list[node1].append(node2)
            my_list[node2].append(node1)
        for key,values in my_list.items():
            if len(values) == len(edges) :
                return key
            
        return -1