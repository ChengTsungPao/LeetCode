class Solution {
public:
    int arraySign(vector<int>& nums) {
        int xor_val = 1;
        for(int num: nums){
            xor_val ^= num;
            if(num == 0) return 0;
        }
        return (xor_val >= 0) ? 1 : -1;
    }
};