class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        # 依序上車，到地點後下車，觀察是否超載
        
        car = collections.defaultdict(int)
        for numPassengers, place1, place2 in trips:
            car[place1] += numPassengers
            car[place2] -= numPassengers
        
        curPassengers = 0
        for place in sorted(car.keys()):
            curPassengers += car[place]
            if curPassengers > capacity:
                return False
        
        return True
