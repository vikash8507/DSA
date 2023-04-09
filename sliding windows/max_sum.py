# https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1?page=1&category[]=sliding-window&sortBy=submissions

def maximumSumSubarray (K,Arr,N):

    curr_sum = sum(Arr[:K])
    curr_max = curr_sum
    
    for i in range(K, N):
        curr_sum = curr_sum + Arr[i] - Arr[i-K]
        curr_max = max(curr_sum, curr_max)
    return curr_max


arr = [100, 200, 300, 400]
k = 2
n = len(arr)
print("Answer:", maximumSumSubarray(k, arr, n))