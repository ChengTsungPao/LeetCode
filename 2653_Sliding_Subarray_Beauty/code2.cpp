# include <ext/pb_ds/assoc_container.hpp>
# include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

# define Ordered_set tree<int, null_type,less_equal<int>, rb_tree_tag,tree_order_statistics_node_update>

class Solution {
public:
    vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
        int n = nums.size();
        
        vector<int> ans;
        Ordered_set ordered_set;
        
        for(int i = 0; i < n; i++){
            ordered_set.insert(nums[i]);
            if(i + 1 >= k){
                int num = *ordered_set.find_by_order(x-1);
                ans.push_back((num < 0) ? num : 0);
                
                int key = ordered_set.order_of_key(nums[i - k + 1]);
                auto it = ordered_set.find_by_order(key);
                ordered_set.erase(it);
            }
        }
        
        return ans;
    }
};