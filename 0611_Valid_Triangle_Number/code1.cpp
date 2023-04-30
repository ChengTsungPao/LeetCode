class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        int ans = 0;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                int k = bisect_left(nums, nums[i] + nums[j], j + 1, n - 1);
                ans += k - j - 1;
            }
        }
        
        return ans;
    }
    
    int bisect_left(vector<int>& nums, int target, int left, int right){
        int ans = nums.size();
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(nums[mid] < target){
                left = mid + 1;
            } else {
                ans = mid;
                right = mid - 1;
            }          
        }
        return ans;
    }
    
};