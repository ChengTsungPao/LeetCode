class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0){
            return 1;
        }
        return (n > 0) ? positivePow(x, n) : 1 / positivePow(x, -(n + 1)) / x;
    }
    
    double positivePow(double x, int n) {
        if(n == 0){
            return 1;
        }
        int times = 1;
        double ans = x;
        while(times <= n / 2){
            ans = ans * ans;
            times *= 2;
        }
        return ans * positivePow(x, n - times);
    }
};