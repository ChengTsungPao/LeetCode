class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int sum = 0, n = nums.size();
        for(int i = 0; i < n; i++){
            sum += (n % (i + 1) == 0) * nums[i] * nums[i];
        }
        return sum;        
    }
};