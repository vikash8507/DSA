# https://practice.geeksforgeeks.org/problems/preorder-traversal/1?page=1&category[]=Tree&sortBy=submissions

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def preorder(root):
   
    res = []

    if root:
        res.append(root.data)
        res += preorder(root.left)
        res += preorder(root.right)

    return res