class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        status = {}
        for i in range(len(arr)):
            status[i, i] = arr[i]
            for j in range(i + 1, len(arr)):
                status[i, j] = status[i, j - 1] ^ arr[j]
        #print(status)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)): 
                for k in range(j, len(arr)): 
                    if status[i, j - 1] == status[j, k]:
                        ans += 1
        return ans
