# https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def removeDuplicates(head: Node):

    if head is None or head.next is None:
        return head
    
    curr = head
    while curr and curr.next:
        if curr.data != curr.next.data:
            curr = curr.next
        else:
            curr.next = curr.next.next
    return head
