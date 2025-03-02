def construct_adjacency_matrix(edges, n):
    return [[1 if (i + 1, j + 1) in edges else 0 for j in range(n)] for i in range(n)]


def inorder_traversal(tree, node):
    if node not in tree:
        return []

    left = inorder_traversal(tree, tree[node][0]) if tree[node] else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []

    return left + [node] + right

edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
n = 8
adj_matrix = construct_adjacency_matrix(edges, n)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

tree = {
    1: [2, 3],
    2: [5, 6],
    3: [4],
    4: [8],
    5: [7],
    6: [],
    7: [],
    8: []
}

label = int(input("Enter the node label to print subtree in Inorder: "))
inorder_result = inorder_traversal(tree, label)
print(f"Inorder Traversal of subtree rooted at node {label}: {inorder_result}")
