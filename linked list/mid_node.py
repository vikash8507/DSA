# https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1?page=1&category[]=Linked%20List&sortBy=submissions

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head: Node):
        # Code here
        # return the value stored in the middle node
        if head is None or head.next is None:
            return head

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data