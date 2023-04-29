// time: O(n + mloglogm), where m is max element in grid
// space: O(m)

class Solution {
public:
    int diagonalPrime(vector<vector<int>>& nums) {
        
        int n = nums.size(), maxVal = 0;
        for(int i = 0; i < n; i++){
            maxVal = max(maxVal, max(nums[i][i], nums[i][n - i - 1]));
        }
        
        vector<bool> isPrime(maxVal + 1, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for(int i = 2; i * i <= maxVal; i++){
            if(isPrime[i]){
                for(int j = i * i; j <= maxVal; j += i){
                    isPrime[j] = false;
                }
            }
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            int num1 = nums[i][i], num2 = nums[i][n - i - 1];
            if(isPrime[num1]) ans = max(ans, num1);
            if(isPrime[num2]) ans = max(ans, num2);
        }
        
        return ans;
    }
};