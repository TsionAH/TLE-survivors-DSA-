class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:

        # Find root node
        children = set(leftChild + rightChild)
        children.discard(-1)

        roots = []
        for i in range(n):
            if i not in children:
                roots.append(i)

        if len(roots) != 1:
            return False

        root = roots[0]

        visited = set()

        def dfs(node):
            if node == -1:
                return True

            if node in visited:
                return False

            visited.add(node)

            return (dfs(leftChild[node])
                    and dfs(rightChild[node]))

        return dfs(root) and len(visited) == n