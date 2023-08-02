class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        
        vector<int> arr1 = nums;
        vector<vector<int>> ans;
        ans.push_back(nums);
        
        for(int k = 0; k < factorial(n) - 1; k++){
            vector<int> arr2 = arr1;
            
            int i = n - 2;
            while(i >= 0 && arr2[i] >= arr2[i + 1]) i--;            
            reverse(arr2.begin() + i + 1, arr2.end());
            
            if(i >= 0){
                int j = upper_bound(arr2.begin() + i + 1, arr2.end(), arr2[i]) - arr2.begin();
                swap(arr2[i], arr2[j]);
            }
            
            arr1 = arr2;
            ans.push_back(arr2);
        }
        
        return ans;
    }
    
    int factorial(int n){
        int ans = 1;
        for(int i = 1; i <= n; i++){
            ans *= i;
        }
        return ans;
    }
    
};