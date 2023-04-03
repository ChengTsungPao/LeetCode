class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        
        // count remainder
        unordered_map<int, int> count;
        for(int num: nums){
            count[(num % value + value) % value] += 1;
        }

        // get min remainder
        int minR = -1, minCount = INT_MAX;
        for(int r = 0; r < value; r++){
            if(count[r] == 0){
                return r;
            }
            
            if(count[r] < minCount){
                minCount = count[r];
                minR = r;
            }
        }
        
        return minR + minCount * value;
    }
};