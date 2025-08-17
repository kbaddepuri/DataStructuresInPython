
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def dfs(root):
            if not root:
                res.append('null')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        res = []
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        def dfs():
            val = next(values)
            if val == 'null':
                return None
            node= TreeNode(str(val))
            node.left = dfs()
            node.right = dfs()
            return node
        values = iter(values)
        return dfs()