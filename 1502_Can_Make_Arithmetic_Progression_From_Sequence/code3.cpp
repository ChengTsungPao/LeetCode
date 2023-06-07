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
        
        int d = (_max - _min) / (n - 1);
        
        int i = 0;
        while(i < n){
            int num = arr[i];
            
            if(_min + i * d == num){
                i += 1;

            } else if((num - _min) % d > 0){
                return false;
            
            } else {
                int j = (num - _min) / d;
                if(arr[i] == arr[j]) {
                    return false;
                }
                
                swap(arr[i], arr[j]);
            }
        }
        
        return true;
    }
};