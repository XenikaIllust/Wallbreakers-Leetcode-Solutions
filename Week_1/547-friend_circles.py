class Solution:
    """
    I am still figuring out this problem as I am often getting "Time Exceeded Errors".
    """
    def findCircleNum(self, M: List[List[int]]) -> int:      
        def find_root(node, vertices):
            while vertices[node] != -1:
                node = vertices[node]
                
            return node
            
        width = len(M)
        height = width
        
        unlinked_nodes = []
        vertices = dict()
        root_node_count = 0
        
        for i in range(height):
            unlinked_nodes.append(i)
            vertices[i] = -1
        
        print(vertices)
        
        for i in range(height):
            for j in range(width):
                if len(unlinked_nodes) <= 1:
                    break
                
                if j >= i and M[i][j] == 1:
                    if i == j:
                        continue
                    else:
                        root = find_root(i,vertices)
                        
                        if root != j:
                            vertices[root] = j
                            
                            if j in unlinked_nodes:
                                unlinked_nodes.remove(j)
        
        root_node_list = []
        
        for node in vertices:
            root_node_list.append(find_root(node, vertices))
            
        root_node_set = set(root_node_list)
        
        return len(root_node_set)
