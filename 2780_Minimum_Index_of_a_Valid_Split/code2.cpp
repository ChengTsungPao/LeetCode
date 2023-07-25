class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int n = nums.size();
        
        int dominant = nums[0];
        int count = 1;
        for(int i = 1; i < n; i++){
            count += (nums[i] == dominant) ? 1 : -1;
            if(count == 0) {
                count = 1;
                dominant = nums[i];
            }
        }
        
        int dominant_c = 0;
        for(int i = 0; i < n; i++){
            dominant_c += nums[i] == dominant;
        }
        
        if(dominant_c * 2 <= n){
            return -1;
        }
        
        int cur_c = 0;
        for(int i = 0; i < n - 1; i++){
            cur_c += nums[i] == dominant;
            int left = cur_c, right = dominant_c - cur_c;
            if(left * 2 > (i + 1) && right * 2 > (n - i - 1)){
                return i;
            }
        }
        
        return -1;        
    }
};