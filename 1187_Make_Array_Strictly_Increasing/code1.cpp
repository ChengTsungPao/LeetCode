class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        int m = arr1.size();
        int n = arr2.size();
        
        sort(arr2.begin(), arr2.end());
        
        vector<vector<vector<int>>> memo(m + 1, vector<vector<int>>(n + 1, vector<int>(2, -1)));
        
        // first not change
        int change_n = recur(1, 0, false, memo, arr1, arr2);

        // first change
        int change_y = recur(1, 1, true, memo, arr1, arr2);
        change_y = (change_y != INT_MAX) ? change_y + 1 : INT_MAX;
        
        // get answer
        int ans = min(change_n, change_y);
        return (ans != INT_MAX) ? ans : -1;
    }
    
    int recur(int i, int j, bool preChange, vector<vector<vector<int>>>& memo, vector<int>& arr1, vector<int>& arr2) {
        int m = arr1.size();
        int n = arr2.size();
        
        if(i >= m){
            return 0;
        } else if (j >= n + 1){
            return INT_MAX;
        }
        
        if(memo[i][j][preChange] != -1){
            return memo[i][j][preChange];
        }
        
        int ans = recur(i, j + 1, preChange, memo, arr1, arr2);
        int change_n = INT_MAX, change_y = INT_MAX;
        
        if(!preChange){
            // not change
            change_n = (arr1[i - 1] >= arr1[i]) ? INT_MAX : recur(i + 1, j, false, memo, arr1, arr2);
            
            // change
            change_y = (j >= n || arr1[i - 1] >= arr2[j]) ? INT_MAX : recur(i + 1, j + 1, true, memo, arr1, arr2);
            change_y = (change_y != INT_MAX) ? change_y + 1 : INT_MAX;
            
        } else {
            // not change
            change_n = (arr2[j - 1] >= arr1[i]) ? INT_MAX : recur(i + 1, j, false, memo, arr1, arr2);
            
            // change
            change_y = (j >= n || arr2[j - 1] >= arr2[j]) ? INT_MAX : recur(i + 1, j + 1, true, memo, arr1, arr2);
            change_y = (change_y != INT_MAX) ? change_y + 1 : INT_MAX;
        }
        
        ans = min(ans, min(change_n, change_y));
        
        memo[i][j][preChange] = ans;
        return ans;
    }
    
};