"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root

        return left if left else right

    def lowestCommonAncestorWithParentPointer(self, p, q):
        ancestor = ()

        # Add all ancestors of p to a set
        while p:
            ancestor.add(p)
            p = p.parent

        # Traverse q’s ancestors, and return first common one
        while q:
            if q in ancestor:
                return q
            q = q.parent

        return None # If no LCA found

