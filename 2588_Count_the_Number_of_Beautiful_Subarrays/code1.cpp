class Solution {
public:
    long long beautifulSubarrays(vector<int>& nums) {
        /*
          [4,3,1,2,4]
         0 0 1 1 0 0
         0 0 1 0 1 0
         0 1 0 0 0 1
         
         0 0 1 0 0 0
         0 0 1 1 0 0
         0 1 1 1 1 0
         
           1     1
         2         2
        */
        
        long long ans = 0; 
        int total_xor = 0;
        unordered_map<int, int> count;
        count[total_xor] ++;
        
        for(auto& num: nums){
            total_xor ^= num;
            ans += count[total_xor];
            count[total_xor]++;
        }
        
        return ans;
    }
};