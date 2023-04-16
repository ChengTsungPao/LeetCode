class Solution {
public:
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        unordered_map<int, unordered_map<int, int>> memo;
        return recur(0, k, piles, memo);
    }
    
    int recur(int idx, int k, vector<vector<int>>& piles, unordered_map<int, unordered_map<int, int>>& memo){
        
        if(memo[idx].find(k) != memo[idx].end()){
            return memo[idx][k];
        }
        
        if(k == 0 || idx >= piles.size()){
            return 0;
        }
        
        int sum = 0;
        int ans = recur(idx + 1, k, piles, memo);
        for(int i = 1; i < min((int)piles[idx].size(), k) + 1; i++){
            sum += piles[idx][i - 1];
            ans = max(ans, sum + recur(idx + 1, k - i, piles, memo));
        }
        
        memo[idx][k] = ans;
        return ans;
    }
    
};