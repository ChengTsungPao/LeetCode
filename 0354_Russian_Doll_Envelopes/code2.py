class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key = lambda element: (element[0], -element[1]))
        
        def lengthOfLIS(envelopes):

            array_sorted = []

            for i in range(len(envelopes)):

                index = bisect.bisect_left(array_sorted, envelopes[i][1])

                if index >= len(array_sorted):
                    array_sorted.append(envelopes[i][1])
                else:
                    array_sorted[index] = envelopes[i][1]

            return len(array_sorted)
        
        return lengthOfLIS(envelopes)