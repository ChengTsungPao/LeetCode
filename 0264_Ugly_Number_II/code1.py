class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        # 概念: 維護一個陣列"indexOf2_3_5"，其意義為乘上2、3、5能超過當前最大"ugly number"之最小"ugly number"的index
        # 舉例: uglyNums = [1, 2, 3, 4, 5, 6] => uglyNums[index] * 2 > uglyNums[-1] => indexOf2_3_5[0] = index越小越好 = 3
        # 方法: 更新較小power的index，但出現一樣小的power數值，則index都需要加1
        
        uglyNums = [1]
        indexOf2_3_5 = [0, 0, 0]
        
        for i in range(1, n):
            
            power1 = uglyNums[indexOf2_3_5[0]] * 2
            power2 = uglyNums[indexOf2_3_5[1]] * 3
            power3 = uglyNums[indexOf2_3_5[2]] * 5
            
            uglyNums.append(min(power1, power2, power3))
            
            indexOf2_3_5[0] += power1 == uglyNums[-1]
            indexOf2_3_5[1] += power2 == uglyNums[-1]
            indexOf2_3_5[2] += power3 == uglyNums[-1]
                
        return uglyNums[n - 1]
