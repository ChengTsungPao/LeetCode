class Solution
    def maxScore(self, s str) - int
        status = collections.Counter(s[1])
        left = (s[0] == 0)
        right = status[1]
        ans = 0
        for i in range(1, len(s))
            ans = max(ans, left + right)
            if(s[i] == 0)
                left += 1
            else
                right -= 1
        return ans