class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        
        int countNotOnes = 0;
        for(int num: nums){
            countNotOnes += num != 1;
        }
        if(countNotOnes < n){
            return countNotOnes;
        }

        int i = 0, j = 0;
        int min_len = INT_MAX;
        for(i = 0; i < n; i++){
            int g = nums[i];
            for(j = i + 1; j < n; j++){
                g = gcd(g, nums[j]);
                if(g == 1) break;
            }
            if(g == 1){
                min_len = min(min_len, j - i + 1);
            } else {
                break;
            }
        }

        return (min_len != INT_MAX) ? (min_len - 1) + (n - 1) : -1;        
    }
    
    int gcd(int a, int b){
        if(a < b){
            return gcd(b, a);
        }
        if(a % b == 0){
            return b;
        }
        return gcd(a % b, b);
    }
    
};