# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        if root is None:
            return ""

        tree_str = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                tree_str.append("#")
                continue

            tree_str.append(str(node.val))

            # Add both children, even if one is None
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(tree_str)


    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")

        # Reconstruct the root
        root = TreeNode(int(values[0]))

        queue = deque([root])
        i = 1

        while queue:
            parent = queue.popleft()

            # Reconstruct left child
            if values[i] != "#":
                left_node = TreeNode(int(values[i]))
                parent.left = left_node
                queue.append(left_node)

            i += 1

            # Reconstruct right child
            if values[i] != "#":
                right_node = TreeNode(int(values[i]))
                parent.right = right_node
                queue.append(right_node)

            i += 1

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))