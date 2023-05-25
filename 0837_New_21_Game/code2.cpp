class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        vector<double> memo(k, -1);
        return recur(0, n, k, maxPts, memo);
    }
    
    double recur(int total_point, int n, int k, int maxPts, vector<double>& memo) {
        if(total_point >= k){
            return total_point <= n;
        } 
        
        if(memo[total_point] != -1){
            return memo[total_point];
        }
        
        double ans = 0;
        for(int point = 1; point <= maxPts; point++){
            ans += (double)recur(total_point + point, n, k, maxPts, memo) / maxPts;
        }
        
        memo[total_point] = ans;
        return ans;
    }
    
};