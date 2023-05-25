class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        /*
        F(x  ) = (F(x+1) + F(x+2) + F(x+3) + ...... + F(x+W)           ) / W
        F(x+1) = (         F(x+2) + F(x+3) + ...... + F(x+W) + F(x+1+W)) / W
        
        => F(x) - F(x+1) = (F(x+1) - F(x+1+W)) / W => F(x) = F(x+1) + (F(x+1) - F(x+1+W)) / W
        
        notice => F(x) = (F(x+1) + F(x+2) + F(x+3) + ......  + F(x+W)) / W, when x < k
               => F(x) = F(x+1) + (F(x+1) - F(x+1+W)) / W, when x + 1 < k
        */
        
        vector<double> memo(k, -1);
        return recur(0, n, k, maxPts, memo);
    }

    double recur(int total_point, int n, int k, int maxPts, vector<double>& memo) {
        if(total_point == k - 1){
            return (double)min(n - k + 1, maxPts) / maxPts;
        } else if(total_point >= k){
            return total_point <= n;
        } 
        
        if(memo[total_point] != -1){
            return memo[total_point];
        }
        
        double f_1 = (double)recur(total_point + 1, n, k, maxPts, memo);
        double f_1_W = (double)recur(total_point + 1 + maxPts, n, k, maxPts, memo);
        double ans = f_1 + (f_1 - f_1_W) / maxPts;
        
        memo[total_point] = ans;
        return ans;
    }
};