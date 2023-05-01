class Solution {
public:
    double average(vector<int>& salary) {
        int n = salary.size();
        int sum = 0, max_ = 0, min_ = INT_MAX;
        for(int s: salary){
            max_ = max(max_, s);
            min_ = min(min_, s);
            sum += s;
        }
        return (double)(sum - max_ - min_) / (n - 2);
    }
};