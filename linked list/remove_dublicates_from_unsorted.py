# https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

class Node:
    def __init__(self, data, next: None):
        self.data = data
        self.next = next


class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head: Node):
        # code here
        if head is None or head.next is None:
            return head

        curr = head
        visited = {curr.data: True}

        while curr and curr.next:
            if curr.next.data in visited:
                curr.next = curr.next.next
            else:
                curr = curr.next
                visited[curr.data] = True
        
        return head
