class Solution:
    def diffPossible(self, arr, n):
        size = len(arr) 
        i,j = 0,1
        while i < size and j < size: 
            if i != j and arr[j]-arr[i] == n: 
                return 1
            elif arr[j] - arr[i] < n: 
                j+=1
            else: 
                i+=1
        return 0
