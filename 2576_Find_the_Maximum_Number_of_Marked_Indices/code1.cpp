class Solution {
public:
    int maxNumOfMarkedIndices(vector<int>& nums) {
        /*
        2 * nums[i] <= nums[j]
        
        [.....] [......]
           i k         j
           
        => 切一半 => j比i先跑完 (保證k存在) (k = i + 1 ~ n / 2 - 1)
        => (i ~ k)內部搭配: i * 2 > j > k
        => (0 ~ i)與k搭配，得到更好的結果?? => i * 2 > j不管怎樣配不會更好 (>=i不能與j配)
        
        */
        
        int n = nums.size();
        sort(nums.begin(), nums.end());
        
        int ans = 0;
        int i = 0, j = n / 2;
        while(i < n / 2 && j < n){
            if(nums[i] * 2 > nums[j]){
                j += 1;
                continue;
            }
            ans += 2;
            i += 1;
            j += 1;
        }
        
        return ans;
    }
};