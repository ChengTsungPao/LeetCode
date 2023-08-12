class Solution {
public:
    int memo[101][101];

    bool canSplitArray(vector<int>& nums, int m) {
        int n = nums.size();
        memset(memo, -1, sizeof(memo));
        return recur(0, n - 1, nums, m);
    }

    bool recur(int i, int j, vector<int>& nums, int m){
        if(i >= j){
            return true;
        }

        if(memo[i][j] != -1){
            return memo[i][j];
        }

        int sum = accumulate(nums.begin() + i , nums.begin() + j + 1, 0);
        bool ans = false;
        int leftSum = 0, rightSum = 0;
        for(int k = i; k < j && !ans; k++){
            leftSum += nums[k];
            rightSum = sum - leftSum;
            if((k == i || leftSum >= m) && (k == j - 1 || rightSum >= m)){
                ans = ans || (recur(i, k, nums, m) && recur(k + 1, j, nums, m));
            }
        }

        return memo[i][j] = ans;
    }

};