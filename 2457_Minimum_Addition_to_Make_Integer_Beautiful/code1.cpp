class Solution {
public:
    long long makeIntegerBeautiful(long long n, int target) {

        long pow10 = 10;
        long long num = n;
        
        for(int i = to_string(n).size(); i >= 0 ; i--){
            if(sumDigit(num) <= target){
                break;
            }
            
            num -= num % pow10;
            num += pow10;
            pow10 *= 10;
        }
        
        return num - n;
    }
    
    int sumDigit(long long n){        
        int sum = 0;
        for(auto d: to_string(n)){
            sum += d - '0';
        }
        return sum;
    }
};