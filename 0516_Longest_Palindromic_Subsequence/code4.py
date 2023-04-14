class Solution {
public:
    int longestPalindromeSubseq(string s) {
        unordered_map<int, unordered_map<int, int>> memo;
        int n = s.size();
        return recur(0, n - 1, s, memo);
    }
    
    int recur(int i, int j, string& s, unordered_map<int, unordered_map<int, int>>& memo){
        
        if(memo[i].find(j) != memo[i].end()){
            return memo[i][j];
        }
        
        if(i > j){
            return 0;
        } else if (i == j){
            return 1;
        }
        
        int ans = 0;
        if(s[i] == s[j]){
            ans = max(ans, 2 + recur(i + 1, j - 1, s, memo));
        } else {
            ans = max(ans, max(recur(i + 1, j, s, memo), recur(i, j - 1, s, memo)));
        }
        
        memo[i][j] = ans;
        return ans;
    }
    
};