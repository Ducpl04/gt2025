class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def dfs(self, start, end, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)

        if start == end:
            return True
        
        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                if self.dfs(neighbor, end, visited):
                    return True
        return False
    
    def path_exists(self, start, end):
        return self.dfs(start, end)

def main():
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'd')
    g.add_edge('a', 'd')
    g.add_edge('d', 'e')
    
    start_node = input("Enter the start node: ")
    end_node = input("Enter the end node: ")
    
    if g.path_exists(start_node, end_node):
        print(f"Path exists from {start_node} to {end_node}.")
    else:
        print(f"No path exists from {start_node} to {end_node}.")

if __name__ == "__main__":
    main()