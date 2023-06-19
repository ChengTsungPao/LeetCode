class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans = 0, h = 0;
        for(int dh: gain){
            h += dh;
            ans = max(ans, h);
        }
        return ans;
    }
};