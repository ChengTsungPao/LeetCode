class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        /*
        
        |a + b + c|5   |5 + 0 + 0|
        |+   +   +|    |+   +   +|
        |d + e + f|7   |3 + 4 + 0|
        |+   +   +|    |+   +   +|
        |g + h + i|10  |0 + 2 + 8|
         8   6   8
         
        */
        
        int m = rowSum.size();
        int n = colSum.size();
        
        vector<vector<int>> matrix(m, vector<int>(n, 0));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int minVal = min(rowSum[i], colSum[j]);
                matrix[i][j] = minVal;
                rowSum[i] -= minVal;
                colSum[j] -= minVal;
                if(rowSum[i] == 0) break;
            }
        }
        
        return matrix;
    }
};