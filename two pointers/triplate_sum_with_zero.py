# https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1?page=1&category[]=two-pointer-algorithm&sortBy=submissions

# Inputs
arr = [0, -1, 2, -3, 1]
n = len(arr)


'''
    Time Complexity: O(n2)
    Auxiliary Space: O(1)
'''

def findTriplets(arr, n) -> bool:
    #code here
    sm = 0
    for i in range(n-1):
        temp = set()
        crr_sum = sm-arr[i]
        for j in range(i+1, n):
            if (crr_sum - arr[j]) in temp:
                return True
            temp.add(arr[j])
    return False

print("Answer:", findTriplets(arr, n))