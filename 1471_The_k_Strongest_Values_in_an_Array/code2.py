class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        n = len(arr)
        arr.sort()
        
        m = arr[n // 2] if n % 2 else arr[n // 2 - 1]
        
        def compare(x, y):
            valueX, valueY = abs(x - m), abs(y - m)
            if valueX == valueY:
                return y - x
            else:
                return valueY - valueX
        
        arr.sort(key = functools.cmp_to_key(compare))
                
        return arr[:k]