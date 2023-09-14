class Solution {
public:
    int M = pow(10, 9) + 7;
    
    int countOrders(int n) {
        // Fermat's little theorem: b^(M - 1) ≡ 1 (mod M) => b^(M - 2) ≡ b^(-1) ≡ b_ (mod M) (M is prime)
        
        // calculate a / b, when a = (2n)!, b = 2^n
        long long a = 1;
        for(int i = 2; i <= 2 * n; i++){
            a *= i;
            a %= M;
        }
        int b = myPow(2, n, M);
        int b_ = myPow(b, M - 2, M);
        
        // c ≡ d (mod M) & e ≡ f (mod M) => ce ≡ df (mod M)
        return (a * b_) % M;
    }
    
    int myPow(int x, int n, int M){
        if(n == 0){
            return 1;
        }
        
        long long val = x;
        int times = 1;
        while(times * 2 <= n){
            val *= val;
            val %= M;
            times *= 2;
        }
        return (val * myPow(x, n - times, M)) % M;
    }
};