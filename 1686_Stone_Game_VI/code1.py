class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
        result, data = 0, sorted(zip(aliceValues, bobValues), key = lambda element: - (element[0] + element[1]))
            
        for index, point in enumerate(data):
            if index % 2 == 0:
                result += point[0]
            else:
                result -= point[1]
                
        return 1 * (result != 0 and result // abs(result))