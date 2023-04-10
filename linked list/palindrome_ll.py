# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1?page=1&category[]=Linked%20List&sortBy=submissions

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:

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
    
    def isPalindrome(self, head):
        #code here
        if head is None or head.next is None:
            return True
        
        slow = fast = head
        prev_slow = mid= None
        
        while fast and fast.next:
            fast = fast.next.next
            prev_slow = slow
            slow = slow.next
        if fast is not None:
            mid = slow
            slow = slow.next

        second_half = self.reverseList(slow)
        prev_slow.next = None

        temp1 = head
        temp2 = second_half
        
        while temp1 and temp2:
            if temp1.data == temp2.data:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0
        if temp1 is None and temp2 is None:
            return 1
        return 0