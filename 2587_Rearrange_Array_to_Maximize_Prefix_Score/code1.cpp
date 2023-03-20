class Solution {
public:
    int maxScore(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        
        long long sum = 0;
        int ans = 0; 
        for(auto num: nums){
            sum += num;
            if(sum > 0){
                ans += 1;
            } else {
                break;
            }
        }
        return ans;
    }
};