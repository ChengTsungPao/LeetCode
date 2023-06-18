class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {

        int max_ = nums[0], min_ = nums[0];
        
        for(int num: nums){
            if(num < max_ && num > min_){
                return num;
            }
            if(num > max_){
                if(max_ > min_){
                    return max_;
                }
                max_ = num;
            }
            if(num < min_){
                if(min_ < max_){
                    return min_;
                }
                min_ = num;
            }
        }
        
        return -1;
    }
};