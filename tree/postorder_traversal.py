# https://practice.geeksforgeeks.org/problems/postorder-traversal/1?page=2&category[]=Tree&sortBy=submissions

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def postOrder(root):
   
    res = []

    if root:
        res += postOrder(root.left)
        res += postOrder(root.right)
        res.append(root.data)

    return res