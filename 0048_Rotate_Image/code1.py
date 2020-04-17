class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)-1
        for j in range(length,-1,-1):
            for i in range(length,-1,-1):                
                matrix[j].append(matrix[i].pop(j))