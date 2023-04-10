# https://practice.geeksforgeeks.org/problems/inorder-traversal/1?page=1&category[]=Tree&sortBy=submissions

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def InOrder(self, root: Node):
        res = []
        if root is None:
            return res
        res += self.InOrder(root.left)
        res.append(root.data)
        res += self.InOrder(root.right)
        
        return res