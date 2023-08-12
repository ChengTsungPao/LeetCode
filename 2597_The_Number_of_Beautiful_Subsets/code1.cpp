class Solution{
public:
    int beautifulSubsets(vector<int>& nums, int k){
        int n = nums.size();
        unordered_map<int, int> cache;
        return backtracking(0, cache, nums, k) - 1;
    }

    int backtracking(int idx, unordered_map<int, int>& cache, vector<int>& nums, int k){
        int n = nums.size();

        if(idx >= n){
            return 1;
        }

        int num = nums[idx];
        int ans = backtracking(idx + 1, cache, nums, k);
        if(cache[num + k] == 0 && cache[num - k] == 0){
            cache[num] += 1;
            ans += backtracking(idx + 1, cache, nums, k);
            cache[num] -= 1;
        }

        return ans;
    }

};