class Solution {
public:
    int M = pow(10, 9) + 7;
    int memo[1001][1001];
    
    int numOfWays(vector<int>& nums) {
        /*
        [3, 4, 5, 1, 2]
        [V, X, X, O, O]
            O, O, X, X
            O, X, O, X
            X, O, X, O
            X, O, O, X
            O, X, X, O
        */
        memset(memo, -1, sizeof(memo));
        return recur(nums) - 1;
    }
    
    long long recur(vector<int> nums){
        int n = nums.size();
        
        if(n <= 1){
            return 1;
        }
        
        int rootNum = nums[0];
        vector<int> left, right;
        for(int i = 1; i < n; i++){
            int num = nums[i];
            if(num < rootNum) {
                left.push_back(num);
            } else {
                right.push_back(num);
            }
        }
        
        int k = left.size();
        long long ans = comb(n - 1, k);
        
        ans = (ans * recur(left)) % M;
        ans = (ans * recur(right)) % M;
        
        return ans % M;
    }
    
    // calculate mod combinations
    // Pascal's triangle: comb(n, k) = comb(n - 1, k) + comb(n - 1, k - 1)    
    
    long long comb(int n, int k){
        if(k < 0 || k > n){
            return 0;
        } else if (n <= 1 || k == 0){
            return 1;
        }
        if(memo[n][k] != -1){
            return memo[n][k];
        }
        memo[n][k] = (comb(n - 1, k) + comb(n - 1, k - 1)) % M;
        return memo[n][k];
    }
    
};