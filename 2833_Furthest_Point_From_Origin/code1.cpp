class Solution {
public:
    int furthestDistanceFromOrigin(string moves) {
        int d_L = 0, d_R = 0;
        for(int m: moves){
            d_L += (m == 'L' || m == '_') ? -1 : 1;
            d_R += (m == 'R' || m == '_') ? 1 : -1;
        }
        return max(abs(d_L), abs(d_R));
    }
};