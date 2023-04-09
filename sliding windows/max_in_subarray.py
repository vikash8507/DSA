# https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1?page=1&category[]=sliding-window&sortBy=submissions

# Inputs
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
K = 3


'''
    Time Complexity: O((n-k+1)*k)
    Space Complexity: O(1)
'''

def max_of_subarrays(arr, N, K):
    mx = 0
    res = []
 
    for i in range(N - K + 1):
        mx = arr[i]
        for j in range(1, K):
            if arr[i + j] > mx:
                mx = arr[i + j]
        res.append(mx)

    return res

print("Answer:", max_of_subarrays(arr, N, K))



'''
    Time Complexity: O(N)
    Space Complexity: O(K)
'''

def max_of_subarrays(arr,n,k):
    
    #code here
    queue = []
    result = []

    for i in range(n):
        if (len(queue) == 0) or (queue[len(queue)-1] >= arr[i]):
            queue.append(arr[i])
        else:
            j = len(queue) - 1
            while (j >= 0) and queue[j] < arr[i]:
                j -= 1
                queue.pop()
            queue.append(arr[i])
        if i >= k-1:
            result.append(queue[0])
            if queue[0] == arr[i-k+1]:
                queue.pop(0)
    return result
    
print("Answer:", max_of_subarrays(arr, N, K))