class Solution {
public:
    int minFlips(int a, int b, int c) {
        /*
        abc
        000: 0
        001: 1
        010: 1
        011: 0
        100: 1
        101: 0
        110: 2
        111: 0
        */
        int ans = 0;
        vector<int> flip = {0, 1, 1, 0, 1, 0, 2, 0};
        while(a > 0 || b > 0 || c > 0){
            int d_a = a & 1, d_b = b & 1, d_c = c & 1;
            ans += flip[(d_a << 2) + (d_b << 1) + d_c];
            a >>= 1;
            b >>= 1;
            c >>= 1;
        }
        return ans;        
    }
};