class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int n = nums.size();
        
        int dominant = -1;
        unordered_map<int, int> count;
        for(int num: nums){
            count[num] += 1;
            if(count[num] * 2 > n){
                dominant = num;
            }
        }
        
        if(dominant == -1){
            return -1;
        }
        
        int dominant_c = count[dominant];
        for(int i = 0; i < n - 1; i++){
            dominant_c -= nums[i] == dominant;
            int left = count[dominant] - dominant_c, right = dominant_c;
            if(left * 2 > (i + 1) && right * 2 > (n - i - 1)){
                return i;
            }
        }
        
        return -1;        
    }
};