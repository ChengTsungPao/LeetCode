class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        sort(nums.begin(), nums.end());
        
        int n = nums.size(), maxVal = 0;
        for(int i = 0; i < n - 1; i++){
            maxVal = max(maxVal, abs(nums[i + 1] - nums[i]));
        }
        
        int left = 0, right = maxVal, ans = -1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(condition(nums, p, mid)){
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            
        }
        
        return ans;
    }
    
    // nums is sorted
    bool condition(vector<int>& nums, int p, int val){
        int n = nums.size(), count = 0;
        for(int i = 0; i < n - 1; i++){
            if(abs(nums[i + 1] - nums[i]) <= val){
                count++;
                i++;
            }
        }
        return count >= p;
    }
    
};