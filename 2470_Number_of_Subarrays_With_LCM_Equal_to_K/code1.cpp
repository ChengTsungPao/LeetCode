class Solution {
public:
    int subarrayLCM(vector<int>& nums, int k) {
        
        int n = nums.size();
        
        int ans = 0;
        for(int i = 0; i < n; i++){
            int lcm = nums[i];
            ans += (lcm == k) ? 1 : 0;
            for(int j = i + 1; j < n; j++){
                int new_lcm = lcm * nums[j] / gcd(lcm, nums[j]);
                if(new_lcm == k){
                    ans += 1;
                } else if (new_lcm > k){
                    break;
                }
                
                lcm = new_lcm;
            }
        }
        
        return ans;
    }
    
    int gcd(int a, int b){
        if(a > b){
            swap(a, b);
        }
        if(b % a == 0){
            return a;
        }
        return gcd(b % a, a);
    }
    
};