# https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1?page=1&category[]=two-pointer-algorithm&sortBy=submissions

class Node:
    def _init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


def detectLoop(head: Node) -> bool:
    #code here
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False