class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        
        int n = days.size();
        
        vector<int> dp(n + 1, 0);
        for(int i = n - 1; i >= 0; i--){
            int day = days[i];
            
            int idx1  = getNextIndex(i, day +  1 - 1, days);
            int idx7  = getNextIndex(i, day +  7 - 1, days);
            int idx30 = getNextIndex(i, day + 30 - 1, days);
            
            int cost1  = costs[0] + dp[idx1];
            int cost7  = costs[1] + dp[idx7];
            int cost30 = costs[2] + dp[idx30];
            
            dp[i] = min(min(cost1, cost7), cost30); 
        }
        
        return dp[0];
    }
    
    int getNextIndex(int i, int lastDay, vector<int>& days){
        int n = days.size();
        if(lastDay >= days[n - 1]){
            return n;
        }
        
        int nextIndex = -1;
        int j = n - 1;
        while(i <= j){
            int k = i + (j - i) / 2;
            if(days[k] <= lastDay){
                i = k + 1;
            } else {
                nextIndex = k;
                j = k - 1;
            }
        }
        
        return nextIndex;
    }
    
};