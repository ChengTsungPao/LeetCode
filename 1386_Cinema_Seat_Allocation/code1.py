class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        empty_count = n * 2
        
        rowSeat = collections.defaultdict(set)
        for x, y in reservedSeats:
            rowSeat[x].add(y)
            
        ans = empty_count
        for x in rowSeat.keys():
            seat1 = len({2, 3, 4, 5} & rowSeat[x]) == 0
            seat2 = len({4, 5, 6, 7} & rowSeat[x]) == 0
            seat3 = len({6, 7, 8, 9} & rowSeat[x]) == 0

            if seat1 and seat2 and seat3:
                continue
            elif (seat1 and seat2) or (seat2 and seat3):
                ans -= 1
            elif seat1 and seat3:
                continue
            elif seat1 or seat2 or seat3:
                ans -= 1
            else:
                ans -= 2
  
        return ans