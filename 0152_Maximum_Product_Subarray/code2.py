class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = -float("inf")
        
        product = 1
        positiveMin = float("inf")
        negativeMin = float("inf")
        
        for num in nums:
            if num == 0:
                product = 1
                positiveMin = float("inf")
                negativeMin = float("inf")
                ans = max(ans, 0)
            else:
                product *= num
                ans = max(ans, product)
                
                if product > 0:
                    if positiveMin == float("inf"):
                        positiveMin = product
                    else:
                        ans = max(ans, product // positiveMin)
                        positiveMin = min(positiveMin, product)
                else:
                    if negativeMin == float("inf"):
                        negativeMin = product
                    else:
                        ans = max(ans, product // negativeMin)
                        negativeMin = max(negativeMin, product)
                    
        return ans