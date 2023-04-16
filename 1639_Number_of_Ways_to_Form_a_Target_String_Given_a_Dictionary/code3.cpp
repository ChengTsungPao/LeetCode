class Solution {
public:
    int MOD = pow(10, 9) + 7;
    
    int numWays(vector<string>& words, string target) {
        int m = words.size();
        int n = words[0].size();
        vector<vector<int>> countWordIdxCh(n, vector<int>(26, 0));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                char ch = words[i][j];
                countWordIdxCh[j][ch - 'a'] += 1;
            }
        }
        
        unordered_map<int, unordered_map<int, int>> memo;
        return recur(0, 0, target, countWordIdxCh, memo);
    }
    
    int recur(int i, int j, string target, vector<vector<int>>& countWordIdxCh, unordered_map<int, unordered_map<int, int>>& memo){
        
        if(memo[i].find(j) != memo[i].end()){
            return memo[i][j];
        }
        
        if(i >= target.size()){
            return 1;
        } else if (j >= countWordIdxCh.size() || countWordIdxCh.size() - j < target.size() - i){
            return 0;
        }
        
        char ch = target[i];
        int countCh = countWordIdxCh[j][ch - 'a'];
        
        int ans = recur(i, j + 1, target, countWordIdxCh, memo) % MOD;
        if(countCh > 0){
            ans += ((long long)countCh * recur(i + 1, j + 1, target, countWordIdxCh, memo)) % MOD;
            ans %= MOD;
        }

        memo[i][j] = ans;
        return ans;
    }
    
};