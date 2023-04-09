# https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1?page=1&category[]=sliding-window&sortBy=submissions

# Inputs
arr = [12, -1, -7, 8, -15, 30, 16, 28]
n = len(arr)
k = 3


'''
    Time Complexity: O((n-k+1)*k)
    Space Complexity: O(1)
'''

def printFirstNegativeInteger(arr, n, k):
    res = []
    # Loop for each subarray(window) of size k
    for i in range(0, (n - k + 1)):
        flag = False
        # Traverse through the current window
        for j in range(0, k):
        
            # If a negative integer is found, then
            # it is the first negative integer for
            # current window. Print it, set the flag
            # and break
            if (arr[i + j] < 0):
                res.append(arr[i + j])
                flag = True
                break
         
        # If the current window does not
        # contain a negative integer
        if (not(flag)):
            res.append(0)
    return res


print("Answer:", printFirstNegativeInteger(arr, n, k))



'''
    Time Complexity: O(N)
    Space Complexity: O(K)
'''

from collections import deque

def printFirstNegative(arr, n, k):
 
    # Create an empty deque to store the indices of negative integers
    neg_ind = deque()
    res = []
 
    # Traverse through the array
    for i in range(n):
        # If the deque is not empty and
        # the leftmost element is out of
        # the current window, then remove it from the deque
        if neg_ind and neg_ind[0] == i - k:
            neg_ind.popleft()
 
        # If the current element is negative, add its index to the deque
        if arr[i] < 0:
            neg_ind.append(i)
 
        # If the current window is of size k,
        # print the first negative integer (if present)
        if i >= k - 1:
            # If the deque is not empty,
            # the leftmost element is the first negative integer
            if neg_ind:
                res.append(arr[neg_ind[0]])
            else:
                res.append(0)
    return res


print("Answer:", printFirstNegativeInteger(arr, n, k))
