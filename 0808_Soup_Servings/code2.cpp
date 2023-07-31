class Solution {
public:    
    double soupServings(int n) {
        // 0.25^x < 10^(-5) => x > 8.3~
        
        n = ceil(n / 25.0);
        unordered_map<int, unordered_map<int, double>> memo;
        for(int i = 1; i <= n; i++){
            if(1 - recur(i, i, memo) < 1e-5){
                return 1.0;
            }
        }
        return recur(n, n, memo);
    }
    
    double recur(int A, int B, unordered_map<int, unordered_map<int, double>>& memo) {
        if(A <= 0){
            return (B <= 0) ? 0.5 : 1;
        } else if (B <= 0){
            return 0;
        }
        
        if(memo.find(A) != memo.end() && memo[A].find(B) != memo[A].end()){
            return memo[A][B];
        }
        return memo[A][B] = 0.25 * (recur(A - 4, B, memo) + recur(A - 3, B - 1, memo) + recur(A - 2, B - 2, memo) + recur(A - 1, B - 3, memo));
    }
    
};