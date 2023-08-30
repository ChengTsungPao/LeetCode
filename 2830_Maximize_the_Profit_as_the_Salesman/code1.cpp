class Solution {
public:
    int memo[100001];
    
    int maximizeTheProfit(int n, vector<vector<int>>& offers) {
        sort(offers.begin(), offers.end());
        memset(memo, -1, sizeof(memo));
        return recur(0, offers);
    }
    
    int recur(int idx, vector<vector<int>>& offers){
        int n = offers.size();
        
        if(idx >= n){
            return 0;
        }
        
        if(memo[idx] != -1){
            return memo[idx];
        }
        
        int start = offers[idx][0], end = offers[idx][1], gold = offers[idx][2];
        vector<int> vec = {end, INT_MAX, INT_MAX};
        int nextIdx = upper_bound(offers.begin() + idx, offers.end(), vec) - offers.begin();
        
        int ans = max(recur(idx + 1, offers), gold + recur(nextIdx, offers));
        return memo[idx] = ans;
    }
    
    
};