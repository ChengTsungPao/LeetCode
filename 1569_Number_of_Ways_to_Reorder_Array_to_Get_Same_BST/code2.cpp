class Solution {
public:
    int M = pow(10, 9) + 7;
    
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
        long long ans = comb(n - 1, k, M);
        
        ans = (ans * recur(left)) % M;
        ans = (ans * recur(right)) % M;
        
        return ans % M;
    }
    
    // calculate mod combinations
    // Fermat's little theorem: a^(M - 1) ≡ 1 (mod M) => a^(M - 2) ≡ a^(-1) (mod M)
    
    long long myPow(int a, int p, int M){
        if(p == 0){
            return 1;
        }
        int times = 1;
        long long val = a;
        while(times * 2 <= p){
            val *= val;
            val %= M;
            times *= 2;
        }
        return (val * myPow(a, p - times, M)) % M;
    }
    
    long long comb(int n, int k, int M){
        long long a = 1;
        for(int i = n; i > n - k; i--){
            a *= i;
            a %= M;
        }
        long long b = 1;
        for(int i = 2; i <= k; i++){
            b *= i;
            b %= M;
        }
        return (a * myPow(b, M - 2, M)) % M;
    }
    
};