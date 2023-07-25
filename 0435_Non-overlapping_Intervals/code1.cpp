class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        
        int ans = 0;
        int minEnd = intervals[0][0];
        for(auto& interval: intervals){
            int start = interval[0], end = interval[1];
            if(minEnd > start){
                minEnd = min(minEnd, end);
                ans += 1;
            } else {
                minEnd = end;
            }
        }
        return ans;
    }
};