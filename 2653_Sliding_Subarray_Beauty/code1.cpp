class Solution {
public:
    vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
        int n = nums.size();
        
        vector<int> ans;
        multiset<int> setx, setr;
        
        for(int i = 0; i < n; i++){
            setx.insert(nums[i]);
            if(setx.size() > x){
                int num = *setx.rbegin();
                setx.erase(setx.find(num));
                setr.insert(num);
            }
            
            if(setx.size() + setr.size() >= k){
                ans.push_back((*setx.rbegin() < 0) ? *setx.rbegin() : 0);
                
                int num = nums[i - k + 1];
                if(setx.find(num) != setx.end()){
                    setx.erase(setx.find(num));
                } else {
                    setr.erase(setr.find(num));
                }
                
                if(setx.size() < x && !setr.empty()){
                    int num = *setr.begin();
                    setr.erase(setr.begin());
                    setx.insert(num);
                }
            }
        }
        
        return ans;
    }
};