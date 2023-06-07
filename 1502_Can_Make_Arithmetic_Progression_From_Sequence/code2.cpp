class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        int n = arr.size();
        int _max = *max_element(arr.begin(), arr.end());
        int _min = *min_element(arr.begin(), arr.end());
        
        if(_max - _min == 0){
            return true;
        } else if ((_max - _min) % (n - 1) > 0) {
            return false;
        }
        
        unordered_set<int> cache;
        int d = (_max - _min) / (n - 1);

        for(int num: arr) {
            if((num - _min) % d > 0){
                return false;
            }
            cache.insert(num);
        }
        return cache.size() == n;
    }
};