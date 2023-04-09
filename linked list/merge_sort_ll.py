# https://practice.geeksforgeeks.org/problems/sort-a-linked-list/1?page=3&category[]=Linked%20List&category[]=doubly-linked-list&category[]=circular-linked-list&category[]=circular%20linked%20list&sortBy=submissions

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def midOfList(self, head):
        if head is None:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeSortedList(self, left, right):
        if not left:
            return right
        if not right:
            return left
        dummy = Node(-1)
        temp = dummy
        while left and right:
            if left.data >= right.data:
                temp.next = right
                right = right.next
                temp = temp.next
            else:
                temp.next = left
                left = left.next
                temp = temp.next
        if left:
            temp.next = left
        if right:
            temp.next = right
        return dummy.next
    
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
    
        mid = self.midOfList(head)
        nextMid = mid.next
        mid.next = None
        
        left = self.mergeSort(head)
        right = self.mergeSort(nextMid)
        
        res = self.mergeSortedList(left, right)
        
        return res
