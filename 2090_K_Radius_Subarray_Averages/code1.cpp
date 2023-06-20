class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int n = nums.size();

        vector<int> ans(n, -1);
        
        long long sum = 0;
        int length = 2 * k + 1;
        
        for(int i = 0; i < n; i++){
            sum += nums[i];
            if(i + 1 >= length){
                ans[i - k] = sum / length;
                sum -= nums[i - length + 1];
            }
        }
        return ans;
    }
};