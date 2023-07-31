class Solution {
public:
    int memo[1001][1001];
    int minimumDeleteSum(string s1, string s2) {
        memset(memo, -1, sizeof(memo));
        return recur(0, 0, s1, s2);
    }
    
    int recur(int i, int j, string& s1, string& s2) {
        int m = s1.size();
        int n = s2.size();
        
        if(memo[i][j] != -1){
            return memo[i][j];
        }
        
        if(i >= m && j >= n){
            return 0;
        } else if (i >= m){
            return memo[i][j] = accumulate(s2.begin() + j, s2.end(), 0);
        } else if (j >= n){
            return memo[i][j] = accumulate(s1.begin() + i, s1.end(), 0);
        }
        
        if(s1[i] == s2[j]){
            return memo[i][j] = recur(i + 1, j + 1, s1, s2);
        } else {
            return memo[i][j] = min(s2[j] + recur(i, j + 1, s1, s2), s1[i] + recur(i + 1, j, s1, s2));
        }
    }
    
};