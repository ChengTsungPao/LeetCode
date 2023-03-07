class Solution {
public:
    vector<int> leftRigthDifference(vector<int>& nums) {
        
        int n = nums.size();
        vector<int> ans(n, 0);
        
        int leftSum = 0, rightSum = 0;
        for(int i = 1; i < n; i++){   
            leftSum += nums[i - 1];
            ans[i] += leftSum;
        }
        for(int i = n - 2; i >= 0; i--){   
            rightSum += nums[i + 1];
            ans[i] -= rightSum;
            ans[i] = abs(ans[i]);
        }
        
        return ans;
    }
};