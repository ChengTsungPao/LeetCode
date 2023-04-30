class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        long long ans = 0;
        long long left = 0, right = (long long)*min_element(ranks.begin(), ranks.end()) * cars * cars;
        while(left <= right){
            long long mid = left + (right - left) / 2;
            if(condition(ranks, mid, cars)){
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
    
    bool condition(vector<int>& ranks, long long time, int cars){
        long long count = 0;
        for(auto rank: ranks){
            count += (long long)sqrt(time / rank);
        }
        return count >= cars;
    }
    
};