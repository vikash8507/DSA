# https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1?page=1&category[]=two-pointer-algorithm&sortBy=submissions


# Inputs
arr = [2, 2, 2, 2, 2]
n = len(arr)


'''
    TC: O(n)
    SC: O(d)
'''

def remove_duplicate(A, N):
    # code here
    res = set(A)
    res = list(res)
    return len(res)

print("Answer:", remove_duplicate(arr, n))


'''
    TC: O(n)
    SC: O(1)
'''

def remove_duplicate(A, N):
    # code here
    i = 1
    while i <= N-1:
        if A[i] == A[i-1]:
            A.pop(i)
            N -= 1
        else:
            i += 1
    return N

print("Answer:", remove_duplicate(arr, n))

