class Solution {
public:
    int averageValue(vector<int>& nums) {
        int sum = 0, count = 0;
        for(auto num: nums){
            if(num % 2 == 0 && num % 3 == 0){
                sum += num;
                count++;
            }
        }
        return (count > 0) ? sum / count : 0;
    }
};