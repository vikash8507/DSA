# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1?page=1&category[]=Linked%20List&sortBy=submissions

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        if head is None or head.next is None:
            return head
            
        prev = None
        nxt = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev