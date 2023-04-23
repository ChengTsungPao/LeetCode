class Solution {
public:
    int minInsertions(string s) {
        int n = s.size();
        vector<vector<int>> memo(n, vector<int>(n, -1));
        return recur(0, n - 1, s, memo);
    }
    
    int recur(int i, int j, string& s, vector<vector<int>>& memo) {
        if(memo[i][j] != -1){
            return memo[i][j];
        }
        
        if(i >= j){
            return 0;
        }
        
        if(s[i] == s[j]){
            memo[i][j] = recur(i + 1, j - 1, s, memo);
        } else {
            memo[i][j] = 1 + min(recur(i + 1, j, s, memo), recur(i, j - 1, s, memo));
        }

        return memo[i][j];
    }
    
};